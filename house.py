# encoding:utf-8
# python3.0

import leancloud
import urllib.request
import time

from anjuke import AnjvkeParser
from ganji import GanjiParser
from lianjia import LianjiaParser
from tongcheng import TongchengParser

# 定义一个getHtml()函数
def getHtml(url):
    # HEADERS = {'cookie':'als=0; sessid=E20EF245-B578-B62A-405F-2E2EC80DD166; ajk_boostup_captcha=0e5106912b04695c71d190f8987ebf1a; ajk_member_captcha=6f503b9a45c529f8f1e53c34c8705def; search_words=%E5%A4%A7%E6%9C%89%E6%81%AC%E5%9B%AD%E4%BA%8C%E6%9C%9F%7C%E5%93%88%E4%BD%9B%E6%98%A0%E5%83%8F%7C%E5%A4%A7%E6%9C%89%E6%81%AC%E5%9B%AD; viewed_comm_21=212476_512034_538146_212341_212176; viewed_comm_list=212511_212476_512034_538146_212341_212176; ajk_member_name=%E8%80%80%E4%B8%AD; ajk_member_key=146c25ce41adc687f802173e10684b46; ajk_member_time=1519886340; aQQ_ajkauthinfos=X%2BvioYvshCNej0r1lQljTMj209xwrTWPFZHr4fU%2BBOVshg2FIa%2FwG804Z%2F5D0RBECPh2dBsrAQ; lui=34603604%3A1; ajk_member_id=34603604; lps=http%3A%2F%2Fdalian.anjuke.com%2F%7C; ctid=21; chatconf=0.1488850300876.2017094.755457675.2005134818.21; browse_comm_ids=512034%7C512033; propertys=chs2vf-omfh2s_cg0a1c-omfbnv_; 58tj_uuid=6bf94a05-49db-441c-a82b-7c6f0fd10568; new_session=0; init_refer=; new_uv=4; __xsptplusUT_8=1; _ga=GA1.2.846449226.1488850146; _gat=1; __xsptplus8=8.4.1488863765.1488864393.3%234%7C%7C%7C%7C%7C%23%23sBxkSJUmyzzeOfmsql0wujs4qe1wUNkI%23; aQQ_ajkguid=81A92F38-8AFB-3CD1-F259-78F93B4E9AE5; twe=2',}
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib.request.Request(url, headers=HEADERS)
    page = urllib.request.urlopen(req)  # urllib.urlopen()方法用于打开一个URL地址
    html = page.read()  # read()方法用于读取URL上的数据
    return html.decode('UTF-8').replace(u'\xa9', u'').replace("'", "").replace("\r\n", "").replace("\n","")  # 汉字转换及正则匹配无法对换行进行处理及去掉单引号


# 清除leancloud数据
def delete():
    # 初始化leancloud
    leancloud.init("tprA4QlLY29nvh5QmiWsNl0s-gzGzoHsz", "idYvbwv28UfweEIJJ01E8bBb")
    # 开启日志
    # logging.basicConfig(level=logging.DEBUG)
    timestring = time.strftime('%Y%m%d%H', time.localtime(time.time()))
    tablename = 'T' + timestring + 'TheFutureOfHome'
    TestObject = leancloud.Object.extend(tablename)
    test_object = TestObject()
    test_object.destroy()


# 保存到leancloud
def save(webName, houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg):
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


# 链家
def lianjia_save(html):
    lianjia = LianjiaParser()
    houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = lianjia.feed(html)
    save('链家', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)


# 58同城
def tongcheng_save(html):
    tongcheng = TongchengParser()
    houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = tongcheng.feed(html)
    save('58同城', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)


# 安居客
def anjvke_save(html):
    anjvke = AnjvkeParser()
    houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = anjvke.feed(html)
    save('安居客', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)


# 赶集
def ganji_save(url):
    ganji = GanjiParser()
    houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg = ganji.feed(html)
    save('赶集', houseName, villageName, houseNote, houseTotlePrice, houseUnitPrice, houseLink, houseImg)


# ------主函数------
# 清除数据
delete()

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
#
# # 安居客 高新园区 80-120W 3室 精装修
# anjuke1 = getHtml('''http://dalian.anjuke.com/sale/gaoxinyuanqua/b136-d52-o5/?from_price=80&to_price=120''')
# anjuke2 = getHtml('''http://dalian.anjuke.com/sale/gaoxinyuanqua/b136-d52-o5-p2/?from_price=80&to_price=120''')
# anjuke3 = getHtml('''http://dalian.anjuke.com/sale/gaoxinyuanqua/b136-d52-o5-p3/?from_price=80&to_price=120''')
# anjvke_htmls = [anjuke1, anjuke2, anjuke3]
# for anjvke_html in anjvke_htmls:
#     anjvke_save(anjvke_html)
#
# # 赶集 高新园区 80-120W 3室 精装修
# ganji1 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3q2/''')
# ganji2 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3o2q2/''')
# ganji3 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3o3q2/''')
# ganji_htmls = [ganji1, ganji2, ganji3]
# for ganji_html in ganji_htmls:
#     ganji_save(ganji_html)

print("OVER!!!")
