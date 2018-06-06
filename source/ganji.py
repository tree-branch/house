# encoding:utf-8

from html.parser import HTMLParser

class GanjiParser(HTMLParser):
    def __init__(self):
        super().__init__()
        # 存储中间数据（链家为总房价与单价）
        self.span = ""
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

    # def handle_starttag(self, tag, attrs):
    #     if tag == "span":
    #         self.flag.append("span")
    #     elif tag == "a" and ("data-el", "ershoufang") in attrs and ("class", "") in attrs:
    #         self.flag.append("houseName")
    #         for attr in attrs:
    #             if attr[0] == "href":
    #                 self.houseLink.append(attr[1])
    #     elif tag == "a" and ("data-el", "region") in attrs:
    #         self.flag.append("villageName")
    #     elif tag == "div" and ("class", "houseInfo") in attrs:
    #         self.flag.append("houseNote")
    #     elif tag == "div" and ("class", "totalPrice") in attrs:
    #         self.flag.append("houseTotlePrice_2")
    #     elif tag == "div" and ("class", "unitPrice") in attrs:
    #         self.flag.append("houseUnitPrice_2")
    #     elif tag == "img" and ("class", "lj-lazy") in attrs:
    #         for attr in attrs:
    #             if attr[0] == "alt":
    #                 for attr2 in attrs:
    #                     if attr2[0] == "data-original":
    #                         self.houseImg.append(attr2[1])
    #                         break
    #                 break
    #
    # def handle_data(self, data):
    #     if len(self.flag) != 0:
    #         if self.flag[-1] == "span":
    #             # print(str(data))
    #             self.span = data
    #             self.flag.pop()
    #             if len(self.flag) > 0 and self.flag[-1] == "houseUnitPrice_2":
    #                 self.houseUnitPrice.append(self.span)
    #                 self.flag.pop()
    #         elif self.flag[-1] == "houseName":
    #             # print(str(data))
    #             self.houseName.append(data)
    #             self.flag.pop()
    #         elif self.flag[-1] == "villageName":
    #             # print(str(data))
    #             self.villageName.append(data)
    #             self.flag.pop()
    #         elif self.flag[-1] == "houseNote":
    #             # print(str(data))
    #             self.houseNote.append(data)
    #             self.flag.pop()
    #         elif self.flag[-1] == "houseTotlePrice_2":
    #             # print(str(data))
    #             self.houseTotlePrice.append(self.span + data)
    #             self.span = ""
    #             self.flag.pop()
    #         # elif self.flag[-1] == "houseUnitPrice_2":
    #         #     self.houseUnitPrice.append(self.span + data)
    #         #     self.span = ""
    #         #     self.flag.pop()
    #         # elif self.flag[-1] == "houseLink":
    #         #     print(str(data))
    #         #     self.houseLink.append(data)
    #         #     self.flag.pop()
    #         # elif self.flag[-1] == "houseImg":
    #         #     print(str(data))
    #         #     self.houseImg.append(data)
    #         #     self.flag.pop()

