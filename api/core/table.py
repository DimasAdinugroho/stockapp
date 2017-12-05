import sys
import time
import copy
import Queue
import pymysql
import operator
import threading
import numpy as np
from decouple import config
from utils import code_symbols
from prettytable import PrettyTable

host = config('WEB_HOST')
username = config('WEB_USER')
password = config('WEB_PASS')
db_name = config('WEB_DB')


def sorting(result, colum_indexes):
    '''colum_indexes:
        Time=1, Open=2, High=3, Close=4
        Low=5, Change=6, Volume=7
        TotalVolume=8, Ask=9, Bid=10

    Args:
        result (list of list):  Result
        colum_indexes (list or integer): the index, e.g: 7 or [7, 8]

    Returns:
        T(list of list): Sorted Result

    '''
    if isinstance(colum_indexes, int):
        result = sorted(result, key=lambda x: (x[colum_indexes]), reverse=True)
    elif isinstance(colum_indexes, list):
        list_index = ', '.join('x[{}]'.format(i) for i in colum_indexes)
        args = '({})'.format(list_index)
        result = sorted(result, key=lambda x: eval(args), reverse=True)
    return result


def get_table(symbol, in_queue, lst, exit_event, lock):
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
            config = {
                'host': host, 'user': username,
                'passwd': password, 'db': db_name
            }
            db = pymysql.connect(**config)
            queries = "select * from {} ORDER BY itemTime DESC LIMIT 1;".format(symbol)

            cur = db.cursor()
            cur.execute(queries)
            result = list(cur.fetchone())
            result.insert(0, symbol)
            obj = result
            cur.close()
        except BaseException as e:
            print(e, symbol)

        lock.acquire()
        lst.append(obj)
        lock.release()

if __name__ == '__main__':
    prev_lines = 0  # do not change this line
    number_symbol_in_table = 10  # number of symbol that will be shown in table
    time_sleep = 10  # will print per 30 second

    while True:
        start = time.time()
        in_queue = Queue.Queue()
        result = []
        exit_event = threading.Event()
        lock = threading.Lock()

        workers = []
        for symbol in code_symbols:
            worker = threading.Thread(
                        target=get_table,
                        args=(symbol, in_queue, result, exit_event, lock)
                    )
            worker.daemon = True
            workers.append(worker)

        for worker in workers:
            worker.start()

        for ids in code_symbols:
            in_queue.put(ids)

        in_queue.join()
        exit_event.set()

        for worker in workers:
            worker.join()

        # Volume is on index 7 and totalVolume is on index 8
        sorted_result = sorting(result, [0, 7, 8])
        # to get real time update table
        get_record = sorted_result[:number_symbol_in_table]

        number_of_records = len(get_record)
        total_lines = number_of_records + 3 + 1  # number of records + Borders + Header

        if prev_lines != 0:
            for i in range(prev_lines):
                sys.stdout.write('\033[F')
        prev_lines = total_lines
        end = time.time()
        table = PrettyTable(['Symbol', 'Time', 'Open', 'High', 'Close', 'Low', 'Change', 'Volume', 'TotalVolume', 'Ask', 'Bid'])
        for value in get_record:
            table.add_row(value)
        print(table)
        if time_sleep-(end-start) > 0:
            time.sleep(time_sleep-(end-start))
