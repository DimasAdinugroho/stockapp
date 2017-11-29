#!/usr/bin/python

from __future__ import print_function

import os
import re
import time
import copy
import json
import logging
import datetime
import threading
import pymysql
import psycopg2
from pprint import pprint
from decouple import config

import Queue
# for compatibility to python 2.7
try:
    import urllib.request as httprequest
    import urllib.parse as parse_url
except ImportError:
    import urllib2 as httprequest
    import urllib as parse_url

from utils import TradingTime, code_symbols

# def print(x):
#     pprint(x)

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )
logger = logging.getLogger(__name__)
# url configuration
url = config('BASE_URL')  # change to baseurl
headers = {}  # insert request header

host = config('HOST')
db_name = config('DB')
username = config('DB_USERNAME')
password = config('DB_PASSWORD')


def time_diff(datetime1, datetime2):
    ''' calculate the time differences '''
    h1, m1, s1 = datetime1.hour, datetime1.minute, datetime1.second
    h2, m2, s2 = datetime2.hour, datetime2.minute, datetime2.second
    datetime1_secs = s1 + 60 * (m1 + 60*h1)
    datetime2_secs = s2 + 60 * (m2 + 60*h2)
    return(datetime2_secs - datetime1_secs)


def change_value(value):
    ''' parse currency value to the integer'''
    comp_ = re.compile(r'[0-9.]+')
    if 'K' in value:
        kilo = 1000
        return int(float(comp_.findall(value)[0]) * kilo)
    elif 'M' in value:
        million = 1000000
        return int(float(comp_.findall(value)[0]) * million)
    elif 'B' in value:
        billion = 1000000000
        return int(float(comp_.findall(value)[0]) * billion)
    elif 'T' in value:
        trillion = 1000000000000
        return int(float(comp_.findall(value)[0]) * trillion)
    else:
        return int(float(value))


def change_pct(value):
    ''' remove % in the string '''
    if '+' in value:
        value = value.replace('+', '')
    return value.replace('%', '')


def create_table(db, tablename):
    ''' Create table on database '''
    cur_ = db.cursor()
    query = """
        CREATE TABLE {} (
        itemTime TIMESTAMP NOT NULL,
        itemPrice INT NOT NULL,
        itemChange DECIMAL(5,2),
        itemTurnover BIGINT,
        itemMarketcap BIGINT,
        itemVolume BIGINT,
        itemFreq INT,
        itemAsk INT,
        itemBid INT,
        PRIMARY KEY (itemTime)
        );""".format(tablename, tablename)
    cur_.execute(query)
    db.commit()
    cur_.close()


def check_table(db, tablename):
    ''' check if table exist or not '''
    cur_ = db.cursor()
    query = "SELECT * FROM information_schema.tables WHERE table_name = '{}' LIMIT 1;".format(tablename)
    cur_.execute(query)
    is_exist = cur_.fetchone()
    db.commit()
    cur_.close()
    if is_exist is not None:
        return True
    return False


def db_conn(symbol, operation, payload, db=None, cur_=None):
    ''' Insert row tp db per data '''
    # cur_ = db.cursor()

    # this it the column name in database
    column_name = ', '.join(['(itemTime', 'itemPrice', 'itemChange', 'itemTurnover', 'itemMarketcap', 'itemVolume', 'itemFreq', 'itemAsk', 'itemBid)'])

    # insert payload to column
    price = payload[0]['LAST']
    change = change_pct(payload[0]['PCT'])
    turn_over = change_value(payload[0]['VAL'])
    market_cap = change_value(payload[0]['MKTCap'])
    volume = change_value(payload[0]['VOL'])
    freq = payload[0]['FREQ']
    ask = payload[2][0]['ASKVol']
    bid = payload[2][0]['BIDVol']
    data = '(NOW(), {}, {}, {}, {}, {}, {}, {}, {})'.format(
        price, change, turn_over, market_cap, volume, freq, ask, bid
    )

    query_insert = "INSERT INTO {} {} VALUES {};".format(symbol, column_name, data)
    query_update = "UPDATE {} SET {} WHERE {};"  # unknown
    query_delete = "DELETE FROM {} WHERE {};"  # unknown

    if db is None:
        config = {
                'host': host, 'user': username,
                'password': password, 'db': db_name,
                'cursorclass': pymysql.cursors.DictCursor
            }
        db = pymysql.connect(**config)
    if cur_ is None:
        cur_ = db.cursor()
    if operation == 'insert':
        cur_.execute(query_insert)
    elif operation == 'update':
        cur_.execute(query_update)
    elif operation == 'delete':
        cur_.execute(query_delete)
    db.commit()
    cur_.close()
    db.close()
    # logger.info('query: {} for {}'.format(query_insert, symbol))
    return data


def split_stock(n, symbols):
    from itertools import islice

    symbols = iter(symbols)
    return iter(lambda: tuple(islice(symbols, n)), ())


def get_price_normal(symbol):
    """Get Stock Price per symbol: benchmark 4.5 second

    Args:
        symbol (str): Symbol Name

    Returns:
        Dict: Symbol Detail
    """
    global url, headers

    values = {'code': symbol}
    data = parse_url.urlencode(values)
    data = data.encode('utf-8')  # data should be bytes
    req_ = httprequest.Request(url, data, headers=headers)
    resp = httprequest.urlopen(req_)
    resp_data = resp.read()
    return eval(json.loads(json.dumps(resp_data.decode("utf-8"))))


def get_price_threading(tr_id, symbols, in_queue, lst, exit_event, lock):
    """Get Stock Price per symbol: benchmark 1.83 second

    For every crawling result, will be save automatically into database
    Args:
        symbol (str): Description
        in_queue (Queue): Symbol Name
        lst (list): Result(Symbol Detail)
        exit_event (threading): exit event
        lock (threading): thread lock
    """
    global url, headers
    while True:
        try:
            item = in_queue.get(timeout=2e-2)
            in_queue.task_done()
        except Queue.Empty:
            if exit_event.is_set():
                break
            continue

        try:
            obj = []
            for symb in symbols[item]:
                values = {'code': symb}
                data = parse_url.urlencode(values)
                data = data.encode('utf-8')  # data should be bytes
                req_ = httprequest.Request(url, data, headers=headers)
                resp = httprequest.urlopen(req_)
                resp_data = resp.read()
                result = eval(json.loads(json.dumps(resp_data.decode("utf-8"))))
                response = db_conn(symb, 'insert', result)
                obj.append(response)
        except BaseException as e:
            print(e, symbols)
            continue

        lock.acquire()
        lst.append(obj)
        lock.release()


if __name__ == '__main__':
    # credential for database

    # CONFIGURATION
    sleep_time = 5  # in seconds, sleep time between getting data
    symbol_per_thread = 5  # split symbol evenly per thread
    # END CONFIGURATION

    is_holiday = False
    now = datetime.datetime.now()
    holiday_time = TradingTime.holiday()  # holiday time

    for i in holiday_time:  # check if holiday or not
        if i.year == now.year and i.month == now.month and i.day == now.day:
            is_holiday = True

    if is_holiday is True:
        logger.info('It is holiday time, no trading allowed')
        os._exit(1)

    # connect to database
    config = {
            'host': host, 'user': username,
            'password': password, 'db': db_name,
            'cursorclass': pymysql.cursors.DictCursor
        }
    db = pymysql.connect(**config)
    cur_ = db.cursor()

    # create table if not exist
    for symbol in code_symbols:
        if check_table(db, symbol) is False:
            create_table(db, symbol)
    db.commit()
    db.close()

    session_1 = TradingTime(1, now.weekday())  # this session 1 time
    session_2 = TradingTime(2, now.weekday())  # this session 2 time
    # looping until the end of session
    while now.hour <= session_2.end.hour and now.minute <= session_2.end.minute:
        # if time between session 1 end and session 2 start, it will continue to sleep
        now = datetime.datetime.now()  # update now variable
        if now.hour <= session_2.start.hour and now.minute <= session_2.start.minute and now.hour >= session_1.start.hour and now.minute >= session_1.start.minute:
            pass
        else:
            start = time.time()  # counting start time
            '''RUN SCRIPT'''
            i = 0
            copy_code_symbols = copy.deepcopy(code_symbols)

            # For every symbol will start new threading and execute function concurrently
            iter_symbol = {}
            iter_thread_id = []
            for index, i in enumerate(split_stock(symbol_per_thread, copy_code_symbols)):
                iter_symbol[index] = list(i)

            in_queue = Queue.Queue()
            result = []
            exit_event = threading.Event()
            lock = threading.Lock()

            workers = []
            for thread_id, symbols in iter_symbol.items():
                worker = threading.Thread(
                            target=get_price_threading,
                            args=(thread_id, iter_symbol, in_queue, result, exit_event, lock)
                        )
                worker.daemon = True
                workers.append(worker)
                iter_thread_id.append(thread_id)

            for worker in workers:
                worker.start()

            for ids in iter_thread_id:
                in_queue.put(ids)

            in_queue.join()
            exit_event.set()

            for worker in workers:
                worker.join()
            '''END THREAD'''
            end = time.time()  # couting end time
            logger.info("execution time: {} on {}".format(end - start, now))
        time.sleep(sleep_time)
    logger.info("Program Terminate")
