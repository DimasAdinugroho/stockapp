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
from pprint import pprint
from decouple import config

from django.utils.dateparse import parse_datetime


config = {
        'host': host, 'user': username,
        'password': password, 'db': db_name,
        'cursorclass': pymysql.cursors.DictCursor
    }
column_name = ', '.join([
                    '(itemTime', 'itemOpen', 'itemClose', 'itemHigh',
                    'itemLow', 'itemChange', 'itemVolume',
                    'itemTotalVolume', 'itemAsk', 'itemBid)'
                ])


# def strtodate(itemtime):
#     return parse_datetime(itemtime)
def create_new_table(db, tablename):
    ''' Create table on database '''
    cur_ = db.cursor()
    query = """
        CREATE TABLE {} (
        itemTime TIMESTAMP NOT NULL,
        itemOpen INT NOT NULL,
        itemClose INT NOT NULL,
        itemHigh INT NOT NULL,
        itemLow INT NOT NULL,
        itemChange DECIMAL(5,2),
        itemVolume BIGINT,
        itemTotalVolume BIGINT,
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


# period in minutes
def get_price_threading(symbol, payload, period=None):
    start_time = datetime.datetime.now()
    minute_prev = start_time.minute
    end_trading_time = datetime.time(hour=17, minute=0, second=0)

    while time_diff(now, session_2.end) >= 0:
        # if time between session 1 end and session 2 start, it will continue to sleep
        now = datetime.datetime.now()  # update now variable

        result = latest_data
        counter = 0

        if time_diff(now, session_1.end) <= 0 and time_diff(now, session_2.start) >= 0:
            pass
        else:
            if now.minute < (minute_prev + period):
                if counter == 0:
                    data = {}
                    now = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
                    data['itemtime'] = now

                    data['open'] = payload[0]['LAST']
                    data['close'] = payload[0]['LAST']
                    data['high'] = payload[0]['LAST']
                    data['low'] = payload[0]['LAST']
                    data['change'] = change_pct(payload[0]['PCT'])
                    data['volume'] = 0
                    data['volume_total'] = change_value(payload[0]['VOL'])
                    data['itemask'] = payload[2][0]['ASKVol']
                    data['itembid'] = payload[2][0]['BIDVol']

                    counter += 1
                    result = '({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(
                        data['itemtime'], data['open'], data['close'], data['high'], data['low'], data['change'], data['volume'], data['volume_total'], data['itemask'], data['itembid']
                    )
                    db = pymysql.connect(**config)
                    query_insert = "INSERT INTO {} {} VALUES {};".format(symbol, column_name, result)
                    cur_.execute(query_insert)
                    db.commit()
                    cur_.close()
                    db.close()
                else:
                    # get last row
                    query_select = "select * from {} ORDER BY itemTime DESC LIMIT 1;".format(symbol)
                    db = pymysql.connect(**config)
                    cur_.execute(query_select)
                    last_data = cur_.fetchone()

                    if last_data[3] > payload[0]['LAST']:  # high
                        last_data[3] = payload[0]['LAST']
                    if last_data[4] < payload[0]['LAST']:  # low
                        last_data[4] = payload[0]['LAST']

                    last_data[6] = change_value(payload[0]['VOL']) - last_data[6]  # volume
                    last_data[7] = change_value(payload[0]['VOL'])  # volume total
                    last_data[8] = payload[2][0]['ASKVol']  # ask
                    last_data[9] = payload[2][0]['BIDVol']  # bid

                    # update the database
                    query_update = """UPDATE {}
                        SET itemHigh={}, itemLow={},itemVolume={},itemTotalVolume={},
                        itemAsk={},itemBid={} ORDER BY itemTime DESC LIMIT 1;
                        """.format(symbol, last_data[3], last_data[4], last_data[6], last_data[7], last_data[8], last_data[9])
                    db = pymysql.connect(**config)
                    cur_.execute(query_update)
                    db.commit()
                    cur_.close()
                    db.close()

                last_result = copy.deepcopy(result)
            else:
                data = {}
                query_select = "select * from {} ORDER BY itemTime DESC LIMIT 1;".format(symbol)
                db = pymysql.connect(**config)
                cur_.execute(query_select)
                last_data = cur_.fetchone()

                now = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
                data['close'] = last_data[2]
                data['itemtime'] = now
                data['open'] = result['itemprice']
                data['high'] = result['itemprice']
                data['low'] = result['itemprice']
                data['close'] = result['itemprice']
                data['volume'] = 0
                data['volume_total'] = result['itemvolume']
                data['itemask'] = result['itemvolume']
                data['itembid'] = result['itemvolume']
                result = '({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(
                    data['itemtime'], data['open'], data['close'], data['high'], data['low'], data['change'], data['volume'], data['volume_total'], data['itemask'], data['itembid']
                )
                db = pymysql.connect(**config)
                query_insert = "INSERT INTO {} {} VALUES {};".format(symbol, column_name, result)
                cur_.execute(query_insert)
                db.commit()
                cur_.close()
                db.close()
                minute_prev = now.minute

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
    # exist, if it is holiday
    if is_holiday is True:
        logger.info('It is holiday time, no trading allowed')
        os._exit(1)

    # exist, if sunday or saturday
    if now.weekday() in [5, 6]:
        logger.info('It is saturday or sunday, no trading allowed')
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
        if check_table(db, symbol+'_1') is False:
            create_new_table(db, symbol+'_1')
    db.commit()
    db.close()

    session_1 = TradingTime(now.weekday(), 1)  # this session 1 time
    session_2 = TradingTime(now.weekday(), 2)  # this session 2 time

    # looping until the end of session
