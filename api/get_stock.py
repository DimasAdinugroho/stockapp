#!/usr/bin/python

import re
import time
import json
import queue
import threading
import MySQLdb
import psycopg2
import urllib.request
from pprint import pprint
from decouple import config

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


def change_value(value):
    ''' parse value to the integer'''
    comp_ = re.compile(r'[0-9.]+')
    if 'T' in value:
        trillion = 1000000000000
        return int(float(comp_.findall(value)[0]) * trillion)
    elif 'B' in value:
        billion = 1000000000
        return int(float(comp_.findall(value)[0]) * billion)
    if 'M' in value:
        million = 1000000
        return int(float(comp_.findall(value)[0]) * million)


def change_pct(value):
    ''' remove % in the string '''
    if '+' in value:
        value = value.replace('+', '')
    return value.replace('%', '')


def create_table(db, tablename):
    cur_ = db.cursor()
    query = """
        DROP TABLE IF EXISTS {}; CREATE TABLE {} (
        itemTime TIMESTAMP NOT NULL,
        itemPrice INT NOT NULL,
        itemChange NUMERIC,
        itemTurnover BIGINT,
        itemMarketcap BIGINT,
        itemVolume BIGINT,
        itemFreq INT,
        itemAsk INT,
        itemBid INT,
        PRIMARY KEY (itemTime)
        );""".format(tablename, tablename)
    cur_.execute(query)
    cur_.close()
    db.commit()


def checK_table(db, tablename):
    ''' check if table exist or not '''
    cur_ = db.cursor()
    query = "SELECT * FROM information_schema.tables WHERE table_name = '{}' LIMIT 1;".format(tablename)
    cur_.execute(query)
    is_exist = cur_.fetchone()
    cur_.close()
    if is_exist is not None:
        return True
    return False


def db_conn(db, symbol: str, operation: str, payload: dict):

    cur_ = db.cursor()
    comp_ = re.compile(r'd\+')  # get only number only

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

    if operation == 'insert':
        cur_.execute(query_insert)
    elif operation == 'update':
        cur_.execute(query_update)
    elif operation == 'delete':
        cur_.execute(query_delete)
    print(cur_)
    db.commit()
    cur_.close()


def get_price_normal(symbol: str):
    """Get Stock Price per symbol: benchmark 4.5 second

    Args:
        symbol (str): Symbol Name

    Returns:
        Dict: Symbol Detail
    """
    global url, header

    values = {'code': symbol}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')  # data should be bytes
    req_ = urllib.request.Request(url, data, headers=headers)
    resp = urllib.request.urlopen(req_)
    resp_data = resp.read()
    return eval(json.loads(json.dumps(resp_data.decode("utf-8"))))


def get_price_threading(db, symbol, in_queue, lst, exit_event, lock):
    """Get Stock Price per symbol: benchmark 1.83 second

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
        except queue.Empty:
            if exit_event.is_set():
                break
            continue

        try:
            values = {'code': symbol}
            data = urllib.parse.urlencode(values)
            data = data.encode('utf-8')  # data should be bytes
            req_ = urllib.request.Request(url, data, headers=headers)
            resp = urllib.request.urlopen(req_)
            resp_data = resp.read()
            result = eval(json.loads(json.dumps(resp_data.decode("utf-8"))))
            obj = db_conn(db, symbol, 'insert', result)

        except:
            continue

        lock.acquire()
        lst.append(obj)
        lock.release()


if __name__ == '__main__':
    start = time.time()  # counting start time
    # UNCOMMENT TO use multiprocessing
    # result = get_price_normal('BBCA')
    result = [{'NAME': 'Bank Central Asia Tbk', 'PREV': 21000, 'OPEN': 20825, 'OPENc': 1, 'HIGH': 21300, 'HIGHc': 0, 'LOW': 20825, 'LOWc': 1, 'LAST': 21300, 'LASTc': 0, 'CHG': '+300', 'PCT': '+1.43%', 'FREQ': 5437, 'VOL': '15.63 M', 'VAL': '328.90 B', 'PER': '23.38', 'AVG': '21043.60', 'AVGc': 0, 'MKTCap': '525.15 T'}, {'PERIOD': '', 'DATA': []}, [{'BID': 21050, 'BIDc': 0, 'BIDVol': 90, 'BIDFreq': 1, 'ASK': 21300, 'ASKc': 0, 'ASKVol': 5651, 'ASKFreq': 44}, {'BID': 20925, 'BIDc': 1, 'BIDVol': 2, 'BIDFreq': 1, 'ASK': 21325, 'ASKc': 0, 'ASKVol': 363, 'ASKFreq': 6}, {'BID': 20900, 'BIDc': 1, 'BIDVol': 3313, 'BIDFreq': 17, 'ASK': 21350, 'ASKc': 0, 'ASKVol': 2237, 'ASKFreq': 14}, {'BID': 20875, 'BIDc': 1, 'BIDVol': 3010, 'BIDFreq': 20, 'ASK': 21375, 'ASKc': 0, 'ASKVol': 53, 'ASKFreq': 5}, {'BID': 20850, 'BIDc': 1, 'BIDVol': 929, 'BIDFreq': 24, 'ASK': 21400, 'ASKc': 0, 'ASKVol': 2453, 'ASKFreq': 22}], [{'PRICE': 20825, 'PRICEc': 1, 'VOL': 3013, 'VOLPct': '1.93%', 'FREQ': 130, 'FREQPct': '2.39%'}, {'PRICE': 20850, 'PRICEc': 1, 'VOL': 4922, 'VOLPct': '3.15%', 'FREQ': 84, 'FREQPct': '1.54%'}, {'PRICE': 20875, 'PRICEc': 1, 'VOL': 3470, 'VOLPct': '2.22%', 'FREQ': 163, 'FREQPct': '3.00%'}, {'PRICE': 20900, 'PRICEc': 1, 'VOL': 5665, 'VOLPct': '3.62%', 'FREQ': 214, 'FREQPct': '3.94%'}, {'PRICE': 20925, 'PRICEc': 1, 'VOL': 5602, 'VOLPct': '3.58%', 'FREQ': 254, 'FREQPct': '4.67%'}, {'PRICE': 20950, 'PRICEc': 1, 'VOL': 13595, 'VOLPct': '8.70%', 'FREQ': 774, 'FREQPct': '14.24%'}, {'PRICE': 20975, 'PRICEc': 1, 'VOL': 41481, 'VOLPct': '26.54%', 'FREQ': 1105, 'FREQPct': '20.32%'}, {'PRICE': 21000, 'PRICEc': 2, 'VOL': 18710, 'VOLPct': '11.97%', 'FREQ': 905, 'FREQPct': '16.65%'}, {'PRICE': 21025, 'PRICEc': 0, 'VOL': 5920, 'VOLPct': '3.79%', 'FREQ': 488, 'FREQPct': '8.98%'}, {'PRICE': 21050, 'PRICEc': 0, 'VOL': 6047, 'VOLPct': '3.87%', 'FREQ': 456, 'FREQPct': '8.39%'}, {'PRICE': 21075, 'PRICEc': 0, 'VOL': 5484, 'VOLPct': '3.51%', 'FREQ': 232, 'FREQPct': '4.27%'}, {'PRICE': 21100, 'PRICEc': 0, 'VOL': 8475, 'VOLPct': '5.42%', 'FREQ': 268, 'FREQPct': '4.93%'}, {'PRICE': 21125, 'PRICEc': 0, 'VOL': 3762, 'VOLPct': '2.41%', 'FREQ': 66, 'FREQPct': '1.21%'}, {'PRICE': 21300, 'PRICEc': 0, 'VOL': 30147, 'VOLPct': '19.29%', 'FREQ': 298, 'FREQPct': '5.48%'}]]
    # print(db_conn('/BBCA', 'BBCA', 'BBCA', result))
    # ------------------------

    config = {
        'host': host, 'user': username,
        'password': password, 'database': db_name,
    }

    # db = MySQLdb.connect(
    #     connect_timeout=5,
    #     **config
    # )
    db = psycopg2.connect(**config)
    # create_table(db, 'coba')
    db_conn(db, 'coba', 'insert', result)

    # # UNCOMMENT to use multithreading
    # result = []
    # in_queue = queue.Queue()
    # exit_event = threading.Event()
    # lock = threading.Lock()

    # workers = []
    # for symbol in code_symbols:
    #     worker = threading.Thread(
    #                 target=get_price_threading,
    #                 args=(db, symbol, in_queue, result, exit_event, lock)
    #             )
    #     worker.daemon = True
    #     workers.append(worker)

    # for worker in workers:
    #     worker.start()

    # for symbol in code_symbols:
    #     in_queue.put(symbol)

    # in_queue.join()
    # exit_event.set()

    # for worker in workers:
    #     worker.join()

    # # ------------------------
    # print(result)
    # end = time.time()  # couting end time
    # print("execution time: {}".format(end - start))
