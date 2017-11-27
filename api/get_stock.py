import re
import time
import json
import queue
import threading
import urllib.request
import MySQLdb
from pprint import pprint
from list_symbol import code_symbols
# from multiprocessing import Pool   # uncomment to use multiprocessing
from decouple import config


def print(x):
    pprint(x)

# url configuration
url = config('BASE_URL')  # change to baseurl
headers = {}  # insert request header

host = config('HOST')
db_name = config('DB')
username = config('USERNAME')
password = config('PASSWORD')


def change_value(value):
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
    return value.replace('%', '')


def db_conn(db, symbol: str, operation: str, payload: dict):

    # cur_ = db.cursor()
    comp_ = re.compile(r'd\+')  # get only number only

    # this it the column name in database
    column_name = ', '.join(['(Time', 'Price', 'Change', 'Turnover', 'Marketcap', 'Volume', 'Freq', 'Ask', 'Bid)'])

    # insert payload to column
    timestamp = time.time()
    price = payload[0]['LAST']
    change = change_pct(payload[0]['PCT'])
    turn_over = change_value(payload[0]['VAL'])
    market_cap = change_value(payload[0]['MKTCap'])
    volume = change_value(payload[0]['VOL'])
    freq = payload[0]['FREQ']
    ask = payload[2][0]['ASKVol']
    bid = payload[2][0]['BIDVol']

    data = '({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(
        timestamp, price, change, turn_over, market_cap, volume, freq, ask, bid
    )

    query_insert = "INSERT INTO {} {} VALUES {}".format(symbol, column_name, data)
    query_update = "UPDATE {} SET {} WHERE {}"  # unknown
    query_delete = "DELETE FROM {} WHERE {}"  # unknown

    if operation == 'insert':
        cur_.execute(query_insert)
    elif operation == 'update':
        cur_.execute(query_update)
    elif operation == 'delete':
        cur_.execute(query_delete)

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
    result = get_price_normal('BBCA')
    print(db_conn('BBCA', 'BBCA', 'BBCA', result))
    # ------------------------

    config = {
        'host': host, 'user': username,
        'passwd': password, 'db': db_name,
    }

    db = MySQLdb.connect(
        connect_timeout=5,
        **config
    )

    # UNCOMMENT to use multithreading
    result = []
    in_queue = queue.Queue()
    exit_event = threading.Event()
    lock = threading.Lock()

    workers = []
    for symbol in code_symbols:
        worker = threading.Thread(
                    target=get_price_threading,
                    args=(db, symbol, in_queue, result, exit_event, lock)
                )
        worker.daemon = True
        workers.append(worker)

    for worker in workers:
        worker.start()

    for symbol in code_symbols:
        in_queue.put(symbol)

    in_queue.join()
    exit_event.set()

    for worker in workers:
        worker.join()

    # ------------------------
    # print(result)
    end = time.time()  # couting end time
    print("execution time: {}".format(end - start))
