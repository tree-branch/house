# encoding:utf-8
# python3.0
import source.template as temp
from .read import readData
import time

class reportData():
    '''
    用于读取数据
    '''

    def __init__(self, reportFileName=None):
        if reportFileName is None:
            self._reportFileName = '房屋价格情况统计' + time.strftime('%Y%m%d', time.localtime(time.time()))
        else:
            self._reportFileName = reportFileName

    # 生成数据块
    def _get_table_label(self, id, day, newdata, olddata):
        import pandas as pd
        new = pd.DataFrame()
        down = pd.DataFrame()
        up = pd.DataFrame()
        other = pd.DataFrame()
        for index, row in newdata.iterrows():
            if row.houseLink in olddata.houseLink.tolist():
                if row.houseTotlePrice < olddata[olddata.houseLink == row.houseLink].houseTotlePrice.iloc[0]:
                    down = down.append(row.append(pd.Series({'old_houseTotlePrice': olddata[olddata.houseLink == row.houseLink].houseTotlePrice.iloc[0]})), ignore_index=True)
                elif row.houseTotlePrice > olddata[olddata.houseLink == row.houseLink].houseTotlePrice.iloc[0]:
                    up = up.append(row.append(pd.Series({'old_houseTotlePrice': olddata[olddata.houseLink == row.houseLink].houseTotlePrice.iloc[0]})), ignore_index=True)
                else:
                    other = other.append(row.append(pd.Series({'old_houseTotlePrice': olddata[olddata.houseLink == row.houseLink].houseTotlePrice.iloc[0]})), ignore_index=True)
            else:
                new = new.append(row.append(pd.Series({'old_houseTotlePrice': '-'})), ignore_index=True)
        new['sign'] = '新增'
        down['sign'] = '下降'
        up['sign'] = '上升'
        other['sign'] = '不变'
        result = '''
        <h2>较上%s天</h2>
        <table id="%s" class="display" style="width:100%%">
            <thead>
            <tr>
                <th>升降标志</th>
                <th>房屋名</th>
                <th>房屋备注</th>
                <th>房屋总价</th>
                <th>房屋历史总价</th>
                <th>房屋单价</th>
                <th>小区名</th>
                <th>房屋链接</th>
                <th>来源网站</th>
            </tr>
            </thead>
            <tbody>''' % (day, id)
        result += self._get_tbody_label(new)
        result += self._get_tbody_label(down)
        result += self._get_tbody_label(up)
        result += self._get_tbody_label(other)
        result += '''
            </tbody>
            <tfoot>
            <tr>
                <th>升降标志</th>
                <th>房屋名</th>
                <th>房屋备注</th>
                <th>房屋总价</th>
                <th>房屋历史总价</th>
                <th>房屋单价</th>
                <th>小区名</th>
                <th>房屋链接</th>
                <th>来源网站</th>
            </tr>
            </tfoot>
        </table>'''
        return result

    def _get_tbody_label(self, data):
        result = ''
        for index, row in data.iterrows():
            result += '''
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><a href="%s" target="_blank">%s</a></td>
                <td>%s</td>
            </tr>'''% (row.sign, row.houseName, row.houseNote, row.houseTotlePrice, row.old_houseTotlePrice, row.houseUnitPrice, row.villageName, row.houseLink if row.houseLink[:4]=="http" else "http://" + row.houseLink, row.houseLink, row.webName)
        return result

    # 生成报告文件
    def get_report(self):
        import datetime
        import configparser
        import os

        start = time.perf_counter()
        # 获取参数
        config = configparser.ConfigParser()
        config.read("config.ini")

        # 时间差
        day1 = None
        day7 = None
        day30 = None

        # 表名
        tn0 = None
        tn1 = None
        tn7 = None
        tn30 = None

        # 数据
        data0 = None
        data1 = None
        data7 = None
        data30 = None

        # 获得所有表名
        read = readData(config)
        tablenames = read.read_tablenames()

        # 得到当天，一天前，一周前，一月前的表名
        day = 1
        while True:
            day = day - 1
            if day == -60:
                break
            res = None
            timestring = (datetime.datetime.now() + datetime.timedelta(days=day)).strftime('%Y%m%d')
            for tablename in tablenames:
                if tablename[1:9] == timestring:
                    res = tablename
                    break
            if res is not None:
                if day == 0:
                    tn0 = res
                elif day > -7:
                    tn1 = res
                    day1 = day
                    day = -6
                elif day > -15:
                    tn7 = res
                    day7 = day
                    day = -29
                elif day > -60:
                    tn30 = res
                    day30 = day
                else:
                    break
            elif day == 0:
                raise ValueError("当天数据不存在。")
        if tn0 is not None:
            # 得到当天的数据
            data0 = read.read_data(tn0)
        if tn1 is not None:
            # 得到day1天前的数据
            data1 = read.read_data(tn1)
        if tn7 is not None:
            # 得到day7天的数据
            data7 = read.read_data(tn7)
        if tn30 is not None:
            # 得到day30天的数据
            data30 = read.read_data(tn30)
        result1 = None
        result7 = None
        result30 = None
        if data1 is not None:
            # 较1天结果html
            result1 = self._get_table_label('day1', (-1)*day1, data0, data1)
        if data7 is not None:
            # 较7天结果html
            result7 = self._get_table_label('day7', (-1)*day7, data0, data7)
        if data30 is not None:
            # 较30天结果html
            result30 = self._get_table_label('day30', (-1)*day30, data0, data30)
        end = time.perf_counter()
        html = temp.html_temp % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), str(end-start) + 's', result1, result7, result30)

        f = open(os.path.dirname(__file__) + '''/../reports/''' + self._reportFileName + '.html', 'wb')
        f.write(html.encode('utf-8'))

        return self._reportFileName + '.html'

