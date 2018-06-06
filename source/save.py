# encoding:utf-8

import configparser
import time

from .beike import BeikeParser
from .anjuke import AnjukeParser
from .ganji import GanjiParser
from .lianjia import LianjiaParser
from .tongcheng import TongchengParser


class saveData():
    '''
    用于保存数据
    '''

    def __init__(self, config):
        self._config = config
        pass

    # 清除leancloud数据
    def _delete_leancloud(self):
        import leancloud
        # 初始化leancloud
        leancloud.init(self._config['leancloud']['appid'], self._config['leancloud']['appkey'])
        # 开启日志
        # logging.basicConfig(level=logging.DEBUG)
        timestring = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        tablename = 'T' + timestring + 'TheFutureOfHome'
        TestObject = leancloud.Object.extend(tablename)
        test_object = TestObject()
        test_object.destroy()

    # 保存到leancloud
    def _save_leancloud(self, webName, houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink,
                        houseImg):
        import leancloud
        # 初始化leancloud
        leancloud.init(self._config['leancloud']['appid'], self._config['leancloud']['appkey'])
        # 开启日志
        # logging.basicConfig(level=logging.DEBUG)
        timestring = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        tablename = 'T' + timestring + 'TheFutureOfHome'
        TestObject = leancloud.Object.extend(tablename)
        for i in range(0, len(houseName)):
            test_object = TestObject()
            test_object.set('webName', webName)
            test_object.set('houseName', houseName[i])
            test_object.set('villageName', villageName[i])
            test_object.set('houseNote', houseNote[i])
            test_object.set('houseTotlePrice', houseTotlePrice[i])
            test_object.set('houseUnitPrice', houseUnitPrice[i])
            test_object.set('houseLink', houseLink[i])
            test_object.set('houseImg', houseImg[i])
            try:
                test_object.save()
            except:
                print(
                    "webName:%s\nhouseName:%s\nvillageName:%s\nhouseNote:%s\nhouseTotlePrice:%s\nhouseUnitPrice:%s\nhouseLink:%s\nhouseImg:%s\n" % (
                        webName, houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink,
                        houseImg))
        print(webName + ' saved ' + str(len(houseName)) + ' rows.')

    # 清理mysql数据
    def _delete_mysql(self):
        import pymysql
        # 用于忽略表已存在的警告
        import warnings
        warnings.filterwarnings("ignore")
        host = self._config.get('mysql', 'host')
        port = self._config.getint('mysql', 'port')
        user = self._config.get('mysql', 'user')
        passwd = self._config.get('mysql', 'passwd')
        db = self._config.get('mysql', 'db')

        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cursor = conn.cursor()
        timestring = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        tablename = 'T' + timestring + 'TheFutureOfHome'
        drop_sql = """drop table IF EXISTS %s""" % (tablename)
        drop_rows = cursor.execute(drop_sql)
        print('delete ' + str(drop_rows) + ' rows.')

        conn.commit()
        cursor.close()
        conn.close()

    # 保存到mysql
    def _save_mysql(self, webName, houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink,
                    houseImg):
        import pymysql
        # 用于忽略表已存在的警告
        import warnings
        warnings.filterwarnings("ignore")
        host = self._config.get('mysql', 'host')
        port = self._config.getint('mysql', 'port')
        user = self._config.get('mysql', 'user')
        passwd = self._config.get('mysql', 'passwd')
        db = self._config.get('mysql', 'db')

        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cursor = conn.cursor()

        timestring = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        tablename = 'T' + timestring + 'TheFutureOfHome'
        create_table_sql = """CREATE TABLE IF NOT EXISTS %s (
            Id int auto_increment,
            webName varchar(255),
            houseName varchar(255),
            villageName varchar(255),
            houseNote varchar(255),
            houseTotlePrice varchar(255),
            houseUnitPrice varchar(255),
            houseLink varchar(255),
            houseImg varchar(255),
            primary key(Id)
        )
        ENGINE=InnoDB DEFAULT CHARSET=utf8;""" % (tablename)
        cursor.execute(create_table_sql)

        insert_sql = """insert into %s (webName, houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg) values """ % (
            tablename)
        for i in range(0, len(houseName)):
            if i == 0:
                insert_sql += """('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                    webName, houseName[i], villageName[i], houseNote[i], houseTotlePrice[i], houseUnitPrice[i],
                    houseLink[i], houseImg[i])
            else:
                insert_sql += """,('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                    webName, houseName[i], villageName[i], houseNote[i], houseTotlePrice[i], houseUnitPrice[i],
                    houseLink[i], houseImg[i])
        insert_sql += """;"""
        saved_rows = 0
        if len(houseName) > 0:
            try:
                saved_rows = cursor.execute(insert_sql)
            except:
                print(insert_sql)
        print(webName + ' saved ' + str(saved_rows) + ' rows.')
        conn.commit()
        cursor.close()
        conn.close()

    def deleteOldData(self):
        if self._config['savetype']['type'] == 'mysql':
            self._delete_mysql()
        elif self._config['savetype']['type'] == 'leancloud':
            self._delete_leancloud()

    def _saveData(self, *args):
        if self._config['savetype']['type'] == 'mysql':
            self._save_mysql(*args)
        elif self._config['savetype']['type'] == 'leancloud':
            self._save_leancloud(*args)

    # 贝壳找房
    def beike_save(self, html):
        beike = BeikeParser()
        houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = beike.feed(html)
        self._saveData('贝壳', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)

    # 链家
    def lianjia_save(self, html):
        lianjia = LianjiaParser()
        houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = lianjia.feed(html)
        self._saveData('链家', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)

    # 58同城
    def tongcheng_save(self, html):
        tongcheng = TongchengParser()
        houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = tongcheng.feed(html)
        self._saveData('58同城', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)

    # 安居客
    def anjuke_save(self, html):
        anjuke = AnjukeParser()
        houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = anjuke.feed(html)
        self._saveData('安居客', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)

    # 赶集
    def ganji_save(self, html):
        ganji = GanjiParser()
        houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = ganji.feed(html)
        self._saveData('赶集', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)
