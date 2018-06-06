# encoding:utf-8
# python3.0
import urllib.request

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
