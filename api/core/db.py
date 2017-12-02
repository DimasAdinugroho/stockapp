from __future__ import print_function

import json
import time
import pymysql
import pandas as pd
from decouple import config
try:
    import urllib.request as httprequest
    import urllib.parse as parse_url
except ImportError:
    import urllib2 as httprequest
    import urllib as parse_url

# from utils import code_symbols

host = config('WEB_HOST')
username = config('WEB_USER')
password = config('WEB_PASS')
db_name = config('WEB_DB')
db_table = 'None'
driver = 'mysql'
port = 3306


class StockRequest(object):
    ''' Using API to connect to the database '''
    def __init__(self, host):
        self.base_url = host

    def post(self, symbol, period=None):
        """Get Post request to fetch data

        Args:
            symbol (str): Symbol Name
            period (None, int): Timestamp range, 1m, 5m, 1h, 2h

        Returns:
            dict: list of data
        """
        base_url = self.base_url+'/api/stocks/get/'  # cuman POST
        values = {'symbol': symbol, 'range': period}
        data = parse_url.urlencode(values)
        data = data.encode('utf-8')  # data should be bytes
        req_ = httprequest.Request(base_url, data)
        resp = httprequest.urlopen(req_)
        resp_data = resp.read()
        return eval(json.loads(json.dumps(resp_data.decode("utf-8"))))

    def get(self, symbol, period=None):
        """Get GET request to fetch data

        Args:
            symbol (str): Symbol Name
            period (None, int): Timestamp range, 1m, 5m, 1h, 2h

        Returns:
            dict: list of data
        """
        base_url = self.base_url+'/api/stocks/save/'  # ada GET ama POST
        if period is None:
            req_url = '?symbol={}'.format(symbol)
        else:
            req_url = '?symbol={}&range={}'.format(symbol, period)
        resp = httprequest.urlopen(base_url+req_url)
        resp_data = resp.read()
        return eval(json.loads(json.dumps(resp_data.decode("utf-8"))))


class ReadStock(object):
    ''' Using MySQLDb os pyycopg2 to connect to the database '''
    def __init__(self, **kwargs):
        import MySQLdb
        import psycopg2

        urls = kwargs['data_url']
        driver = kwargs['driver']
        db_name = kwargs['database']
        db_user = kwargs['username']
        db_password = kwargs['password']
        db_port = int(kwargs['port'])
        self.tb_name = kwargs['table']

        if driver == 'mysql':
            config = {
                'host': urls, 'user': db_user, 'port': db_port,
                'passwd': db_password, 'db': db_name
            }
            self.db = MySQLdb.connect(**config)
        elif driver == 'postgresql':
            config = {
                'host': urls, 'user': db_user,
                'password': db_password, 'dbname': db_name
            }
            self.db = psycopg2.connect(**config)

    def query(self, queries=None):
        if queries is None:
            return pd.read_sql("select * from {}".format(self.tb_name), self.db)
        else:
            queries = queries.replace('tablename', self.tb_name)
            return pd.read_sql(queries, self.db)

# resp = StockRequest('http://localhost:8000')
# print(resp.post("Aces"))

# config = {
#         'data_url': host, 'username': username,
#         'password': password, 'database': db_name,
#         'driver': driver, 'table': db_table,
#         'port': port,
#         'cursorclass': pymysql.cursors.DictCursor
#     }

# start = time.time()
# get = ReadStock(**config)
# print(get.query('select *from tablename'))
# print(get.query('select * from tablename where itemTime > date_sub(now(), interval 3 minute) ;'))
# print(get.query("""select * from tablename where itemTime BETWEEN '2017-11-30 10:00:00' AND '2017-11-30 10:25:00' ORDER BY itemPrice DESC;"""))
# print(time.time() - start)
