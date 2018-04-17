# encoding:utf-8

from html.parser import HTMLParser


class TongchengParser(HTMLParser):
    def __init__(self):
        super().__init__()
        # 存储中间数据（58同城为小区名,房屋介绍）
        self.span_a = ""
        # 存储中间数据（58同城为总价）
        self.b = ""
        # 房屋名称
        self.houseName = []
        # 小区名称
        self.villageName = []
        # 房子介绍
        self.houseNote = []
        # 总价
        self.houseTotlePrice = []
        # 单价
        self.houseUnitPrice = []
        # 房屋链接
        self.houseLink = []
        # 第一张图片
        self.houseImg = []
        # 用于标记数据类型
        self.flag = []

    def feed(self, data):
        super().feed(data)
        # 校验数据个数是否统一
        size = len(self.houseName)
        if len(self.houseName) != size or len(self.villageName) != size or len(self.houseNote) != size \
                or len(self.houseTotlePrice) != size or len(self.houseUnitPrice) != size or len(self.houseLink) != size \
                or len(self.houseImg) != size:
            raise ValueError("数据个数不一致：houseName-" + str(len(self.houseName)) + ",villageName-" + str(len(self.villageName)) +
                             ",houseNote-" + str(len(self.houseNote)) + ",houseTotlePrice-" + str(len(self.houseTotlePrice)) +
                             ",houseUnitPrice-" + str(len(self.houseUnitPrice)) + ",houseLink-" + str(len(self.houseLink)) +
                             ",houseImg-" + str(len(self.houseImg)))
        return self.houseName, self.villageName, self.houseNote, self.houseTotlePrice, self.houseUnitPrice, self.houseLink, self.houseImg

    def handle_starttag(self, tag, attrs):
        if tag == "span":
            self.flag.append("span")
        elif tag == "a" and ("tongji_label", "listclick") in attrs:
            self.flag.append("houseName")
            for attr in attrs:
                if attr[0] == "href":
                    self.houseLink.append(attr[1])
                    break
        elif tag == "a" and len(self.flag) >= 1 and self.flag[-1] == "houseNote_2":
            self.flag.append("a")
            self.flag[-2] = 'villageName_2'
        elif tag == "a":
            self.flag.append("a")
        elif tag == "b":
            self.flag.append("b")
        elif tag == "p" and ("class", "baseinfo") in attrs:
            self.flag.append("houseNote_2")
            self.span_a = ''
        elif tag == "p" and ("class", "sum") in attrs:
            self.flag.append("houseTotlePrice_2")
        elif tag == "p" and ("class", "unit") in attrs:
            self.flag.append("houseUnitPrice")
        elif tag == "img":
            for attr in attrs:
                if attr[0] == "data-src":
                    self.houseImg.append(attr[1])
                    break

    def handle_endtag(self, tag):
        if len(self.flag) != 0:
            if tag == "p" and self.flag[-1] == "villageName_2":
                # 此时为villageName的结束
                # print(self.span.encode('GB18030'))
                self.villageName.append(self.span_a.replace(' ', ''))
                self.flag.pop()
                self.span_a = ""
            elif tag == "p" and self.flag[-1] == "houseNote_2":
                # 此时为houseNote的结束
                # print(self.span.encode('GB18030'))
                self.houseNote.append(self.span_a.replace(' ', ''))
                self.flag.pop()
                self.span_a = ""

    def handle_data(self, data):
        if len(self.flag) != 0:
            if self.flag[-1] == "span":
                # print(str(data))
                self.span_a += data.strip()
                self.flag.pop()
            elif self.flag[-1] == "a":
                # print(str(data))
                self.span_a += data.strip()
                self.flag.pop()
            elif self.flag[-1] == "b":
                # print(str(data))
                self.b += data
                self.flag.pop()
            elif self.flag[-1] == "houseName":
                # print(str(data))
                self.houseName.append(data)
                self.flag.pop()
            elif self.flag[-1] == "houseTotlePrice_2" and data.replace(' ', '') != '':
                # print(str(data))
                self.houseTotlePrice.append(self.b + data.replace(' ', ''))
                self.b = ""
                self.flag.pop()
            elif self.flag[-1] == "houseUnitPrice":
                self.houseUnitPrice.append(data)
                self.flag.pop()

