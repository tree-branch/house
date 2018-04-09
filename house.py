# encoding:utf-8
# python3.0

import urllib.request
import time

from anjuke import AnjukeParser
from ganji import GanjiParser
from lianjia import LianjiaParser
from tongcheng import TongchengParser


# 定义一个getHtml()函数
def getHtml(url):
    # HEADERS = {'cookie':'als=0; sessid=E20EF245-B578-B62A-405F-2E2EC80DD166; ajk_boostup_captcha=0e5106912b04695c71d190f8987ebf1a; ajk_member_captcha=6f503b9a45c529f8f1e53c34c8705def; search_words=%E5%A4%A7%E6%9C%89%E6%81%AC%E5%9B%AD%E4%BA%8C%E6%9C%9F%7C%E5%93%88%E4%BD%9B%E6%98%A0%E5%83%8F%7C%E5%A4%A7%E6%9C%89%E6%81%AC%E5%9B%AD; viewed_comm_21=212476_512034_538146_212341_212176; viewed_comm_list=212511_212476_512034_538146_212341_212176; ajk_member_name=%E8%80%80%E4%B8%AD; ajk_member_key=146c25ce41adc687f802173e10684b46; ajk_member_time=1519886340; aQQ_ajkauthinfos=X%2BvioYvshCNej0r1lQljTMj209xwrTWPFZHr4fU%2BBOVshg2FIa%2FwG804Z%2F5D0RBECPh2dBsrAQ; lui=34603604%3A1; ajk_member_id=34603604; lps=http%3A%2F%2Fdalian.anjuke.com%2F%7C; ctid=21; chatconf=0.1488850300876.2017094.755457675.2005134818.21; browse_comm_ids=512034%7C512033; propertys=chs2vf-omfh2s_cg0a1c-omfbnv_; 58tj_uuid=6bf94a05-49db-441c-a82b-7c6f0fd10568; new_session=0; init_refer=; new_uv=4; __xsptplusUT_8=1; _ga=GA1.2.846449226.1488850146; _gat=1; __xsptplus8=8.4.1488863765.1488864393.3%234%7C%7C%7C%7C%7C%23%23sBxkSJUmyzzeOfmsql0wujs4qe1wUNkI%23; aQQ_ajkguid=81A92F38-8AFB-3CD1-F259-78F93B4E9AE5; twe=2',}
    HEADERS = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    HEADERS = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    req = urllib.request.Request(url, headers=HEADERS)
    page = urllib.request.urlopen(req)  # urllib.urlopen()方法用于打开一个URL地址
    html = page.read()  # read()方法用于读取URL上的数据
    return html.decode('UTF-8').replace(u'\xa9', u'').replace("'", "").replace("\r\n", "").replace("\n", "")  # 汉字转换及正则匹配无法对换行进行处理及去掉单引号


# 清除leancloud数据
def delete():
    import leancloud
    # 初始化leancloud
    leancloud.init("tprA4QlLY29nvh5QmiWsNl0s-gzGzoHsz", "6fralNJ21L9HskFfTE2Lxciu")
    # 开启日志
    # logging.basicConfig(level=logging.DEBUG)
    timestring = time.strftime('%Y%m%d%H', time.localtime(time.time()))
    tablename = 'T' + timestring + 'TheFutureOfHome'
    TestObject = leancloud.Object.extend(tablename)
    test_object = TestObject()
    test_object.destroy()


# 保存到leancloud
def save(webName, houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg):
    import leancloud
    # 初始化leancloud
    leancloud.init("tprA4QlLY29nvh5QmiWsNl0s-gzGzoHsz", "idYvbwv28UfweEIJJ01E8bBb")
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
        test_object.save()


# 清理mysql数据
def delete_mysql():
    import pymysql
    # 用于忽略表已存在的警告
    import warnings
    warnings.filterwarnings("ignore")
    host = ''
    port = 3306
    user = ''
    passwd = ''
    db = ''

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
def save_mysql(webName, houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg):
    import pymysql
    # 用于忽略表已存在的警告
    import warnings
    warnings.filterwarnings("ignore")
    host = ''
    port = 3306
    user = ''
    passwd = ''
    db = ''

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

    insert_sql = """insert into %s (webName, houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg) values """ % (tablename)
    for i in range(0, len(houseName)):
        if i == 0:
            insert_sql += """('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (webName, houseName[i], villageName[i], houseNote[i], houseTotlePrice[i], houseUnitPrice[i], houseLink[i], houseImg[i])
        else:
            insert_sql += """,('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (webName, houseName[i], villageName[i], houseNote[i], houseTotlePrice[i], houseUnitPrice[i], houseLink[i], houseImg[i])
    insert_sql += """;"""
    saved_rows = 0
    if len(houseName) > 0:
        saved_rows = cursor.execute(insert_sql)
    print(webName + ' saved ' + str(saved_rows) + ' rows.')
    conn.commit()
    cursor.close()
    conn.close()


# 链家
def lianjia_save(html):
    lianjia = LianjiaParser()
    houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = lianjia.feed(html)
    save_mysql('链家', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)


# 58同城
def tongcheng_save(html):
    tongcheng = TongchengParser()
    houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = tongcheng.feed(html)
    save('58同城', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)


# 安居客
def anjuke_save(html):
    anjuke = AnjukeParser()
    houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = anjuke.feed(html)
    save_mysql('安居客', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)


# 赶集
def ganji_save(html):
    ganji = GanjiParser()
    houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = ganji.feed(html)
    save('赶集', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)


# ------主函数------
# 清除数据
# delete()
delete_mysql()

anjuke1 = getHtml('''https://beijing.anjuke.com/sale/o5/?from_area=60&to_area=100&from_price=200&to_price=600''')
# 链家 （例：北京 0-600万 60-100平） 根据自己需求添加链接
lianjia1 = getHtml('''https://bj.lianjia.com/ershoufang/bp0ep600ba60ea100l3/rs/''')
lianjia2 = getHtml('''https://bj.lianjia.com/ershoufang/pg2l3ba60ea100ep600/''')
lianjia3 = getHtml('''https://bj.lianjia.com/ershoufang/pg3l3ba60ea100ep600/''')
lianjia_htmls = [lianjia1, lianjia2, lianjia3]
for lianjia_html in lianjia_htmls:
    lianjia_save(lianjia_html)

#
# # 58同城 高新园区 80-120W 3室 精装修
# tongcheng1 = getHtml('''http://dl.58.com/gaoxinyuanqu/ershoufang/e3j4/?huansuanyue=80_120&bunengdaikuan=0''')
# tongcheng2 = getHtml('''http://dl.58.com/gaoxinyuanqu/ershoufang/e3j4/pn2/?huansuanyue=80_120&bunengdaikuan=0''')
# tongcheng3 = getHtml('''http://dl.58.com/gaoxinyuanqu/ershoufang/e3j4/pn3/?huansuanyue=80_120&bunengdaikuan=0''')
# tongcheng_htmls = [tongcheng1, tongcheng2, tongcheng3]
# for tongcheng_html in tongcheng_htmls:
#     tongcheng_save(tongcheng_html)

# 安居客 （例：北京 200-600万 60-100平 按最新排序） 根据自己需求添加链接
anjuke1 = getHtml('''https://beijing.anjuke.com/sale/o5/?from_area=60&to_area=100&from_price=200&to_price=600''')
anjuke2 = getHtml('''https://beijing.anjuke.com/sale/o5-p2/?from_area=60&to_area=100&from_price=200&to_price=600#filtersort''')
anjuke3 = getHtml('''https://beijing.anjuke.com/sale/o5-p3/?from_area=60&to_area=100&from_price=200&to_price=600#filtersort''')
anjuke_htmls = [anjuke1, anjuke2, anjuke3]
for anjuke_html in anjuke_htmls:
    anjuke_save(anjuke_html)

# # 赶集 高新园区 80-120W 3室 精装修
# ganji1 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3q2/''')
# ganji2 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3o2q2/''')
# ganji3 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3o3q2/''')
# ganji_htmls = [ganji1, ganji2, ganji3]
# for ganji_html in ganji_htmls:
#     ganji_save(ganji_html)

print("OVER!!!")
