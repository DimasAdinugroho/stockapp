#!/usr/bin/python

from __future__ import print_function

import re
import time
import copy
import json
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

from list_symbol import code_symbols

# def print(x):
#     pprint(x)

# url configuration
url = config('BASE_URL')  # change to baseurl
headers = {}  # insert request header

host = config('HOST')
db_name = config('DB')
username = config('DB_USERNAME')
password = config('DB_PASSWORD')


def time_diff(t1, t2):
    # caveat emptor - assumes t1 & t2 are python times, on the same day and t2 is after t1
    h1, m1, s1 = t1.hour, t1.minute, t1.second
    h2, m2, s2 = t2.hour, t2.minute, t2.second
    t1_secs = s1 + 60 * (m1 + 60*h1)
    t2_secs = s2 + 60 * (m2 + 60*h2)
    return(t2_secs - t1_secs)


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
    return payload


def get_price_normal(symbol):
    """Get Stock Price per symbol: benchmark 4.5 second

    Args:
        symbol (str): Symbol Name

    Returns:
        Dict: Symbol Detail
    """
    global url, header

    values = {'code': symbol}
    data = parse_url.urlencode(values)
    data = data.encode('utf-8')  # data should be bytes
    req_ = httprequest.Request(url, data, headers=headers)
    resp = httprequest.urlopen(req_)
    resp_data = resp.read()
    return eval(json.loads(json.dumps(resp_data.decode("utf-8"))))


def get_price_threading(symbol, in_queue, lst, exit_event, lock, db=None, cur_=None):
    """Get Stock Price per symbol: benchmark 1.83 second

    For every crawling result, will be save automatically into database
    Args:
        symbol (str): Description
        in_queue (Queue): Symbol Name
        lst (list): Result(Symbol Detail)
        exit_event (threading): exit event
        lock (threading): thread lock
    """
    global url, header
    while True:
        try:
            item = in_queue.get(timeout=2e-2)
            in_queue.task_done()
        except Queue.Empty:
            if exit_event.is_set():
                break
            continue

        try:
            values = {'code': item}
            data = parse_url.urlencode(values)
            data = data.encode('utf-8')  # data should be bytes
            req_ = httprequest.Request(url, data, headers=headers)
            resp = httprequest.urlopen(req_)
            resp_data = resp.read()
            result = eval(json.loads(json.dumps(resp_data.decode("utf-8"))))
            obj = db_conn(symbol, 'insert', result)            
        except BaseException as e:
            print(e, symbol)
            continue

        lock.acquire()
        lst.append(obj)
        lock.release()


if __name__ == '__main__':
    # credential for database
    # for compatibility to python 2.7
    config = {
            'host': host, 'user': username,
            'password': password, 'db': db_name,
            'cursorclass': pymysql.cursors.DictCursor
        }
    db = pymysql.connect(**config)
    cur_ = db.cursor()

    # create table if not exist
    for symbol in code_symbols:
        if check_table(db, symbol) == False:
            create_table(db, symbol)
    db.commit()
    db.close()

    sleep_time = 0  # in seconds
    start = time.time()  # counting start time
    end_trading = datetime.time(hour=17)
    now = datetime.datetime.now()

    # UNCOMMENT to use multithreading

    i = 0
    symbol_per_batch = 20
    copy_code_symbols = copy.deepcopy(code_symbols)

    # For every symbol will start new threading and execute function concurrently
    while len(copy_code_symbols) > 0:
        in_queue = Queue.Queue()
        result = []
        exit_event = threading.Event()
        lock = threading.Lock()

        workers = []

        list_of_symbol = code_symbols[i:i+symbol_per_batch]
        for symbol in list_of_symbol:
            worker = threading.Thread(
                        target=get_price_threading,
                        args=(symbol, in_queue, result, exit_event, lock)
                    )
            worker.daemon = True
            workers.append(worker)

        for worker in workers:
            worker.start()

        for symbol in code_symbols[i:i+symbol_per_batch]:
            in_queue.put(symbol)

        in_queue.join()
        exit_event.set()

        for worker in workers:
            worker.join()

        workers = []
        result = []
        in_queue = None
        exit_event = None
        lock = None

        copy_code_symbols = set(copy_code_symbols).difference(code_symbols[i:i+symbol_per_batch])
        i += symbol_per_batch

    end = time.time()  # couting end time
    print("execution time: {}".format(end - start))
    time.sleep(sleep_time)
    now = datetime.datetime.now()
