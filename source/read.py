# encoding:utf-8

import configparser
import time

from .beike import BeikeParser
from .anjuke import AnjukeParser
from .ganji import GanjiParser
from .lianjia import LianjiaParser
from .tongcheng import TongchengParser


class readData():
    '''
    用于读取数据
    '''

    def __init__(self, config):
        self._config = config
        pass

    # 读取 leancloud 表名列表
    def _read_leancloud_tablenames(self):
        import requests
        url = 'https://tpra4qll.api.lncld.net/1.1/schemas'
        head = {
            "X-LC-Id": self._config['leancloud']['appid'],
            "X-LC-Key": self._config['leancloud']['masterkey'] + ',master'
        }
        response = requests.get(url, headers=head)
        tablenames = sorted(list(response.json().keys()), reverse=True)
        return tablenames

    # 读取 leancloud 表数据
    def _read_leancloud_data(self, tablename):
        import requests
        import pandas as pd

        url = 'https://tpra4qll.api.lncld.net/1.1/classes/'
        limit = 200
        skip = 0
        head = {
            "X-LC-Id": self._config['leancloud']['appid'],
            "X-LC-Key": self._config['leancloud']['appkey'],
            "Content-Type": "application/json"
        }
        sign = 1
        data = pd.DataFrame()
        while(sign):
            response = requests.get(url + str(tablename) + '?limit=' + str(limit) + '&skip=' + str(skip), headers=head)
            data = data.append(pd.DataFrame(response.json()["results"]))
            if len(response.json()["results"])==0:
                sign = 0
            skip = skip + limit
        data = data.drop_duplicates(['houseLink'])
        return data

    # 读取 mysql 表名列表
    def _read_mysql_tablenames(self):
        import mysql.connector
        import pandas as pd

        host = self._config.get('mysql', 'host')
        port = self._config.getint('mysql', 'port')
        user = self._config.get('mysql', 'user')
        passwd = self._config.get('mysql', 'passwd')
        db = self._config.get('mysql', 'db')

        conn = mysql.connector.connect(host=host, user=user, password=passwd, database=db, port=port, use_unicode=True)
        get_tableNames_sql = """select table_name from information_schema.tables order by table_name DESC """
        tablenames = pd.read_sql(get_tableNames_sql, conn).iloc[:, 0].tolist()

        return tablenames

    # 读取 mysql 表数据
    def _read_mysql_data(self, tablename):
        import mysql.connector
        import pandas as pd

        host = self._config.get('mysql', 'host')
        port = self._config.getint('mysql', 'port')
        user = self._config.get('mysql', 'user')
        passwd = self._config.get('mysql', 'passwd')
        db = self._config.get('mysql', 'db')

        conn = mysql.connector.connect(host=host, user=user, password=passwd, database=db, port=port, use_unicode=True)
        get_data_sql = """select * from %s""" % tablename
        data = pd.read_sql(get_data_sql, conn)

        return data

    def read_tablenames(self):
        if self._config['savetype']['type'] == 'mysql':
            return self._read_mysql_tablenames()
        elif self._config['savetype']['type'] == 'leancloud':
            return self._read_leancloud_tablenames()

    def read_data(self, tablename):
        if self._config['savetype']['type'] == 'mysql':
            return self._read_mysql_data(tablename)
        elif self._config['savetype']['type'] == 'leancloud':
            return self._read_leancloud_data(tablename)
