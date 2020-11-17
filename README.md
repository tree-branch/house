# house
此为二手房数据,需要新房数据的移步[new_house](https://github.com/tree-branch/new_house)

爬取贝壳找房、链家、安居客、58同城的房源信息，便于广大未买房子的朋友们尽快成为房奴！！！Crawl the house informations of lianjia.com (anjvke.com, 58.com, ganji.com after the update), convenient for the majority of friends who did not buy the house as soon as to become the mortgage slave!!!

## 直接运行
修改config.ini内的mysql链接地址

python3.0及以上版本

python house.py

缺什么包就 pip install ***

## 个性化运行
此程序是把leancloud作为云数据库使用;在 https://leancloud.cn/ 内建立账号;修改config.ini为自己的App ID App KEY

python house.py

修改house.py内贝壳找房等网站的网址，查询的限定条件需要能够保存在URL内，例如链家的排序也是可以保存在URL内的，一看例子你也应该就懂了，不懂的话就再看一遍，直接给我发邮件当然是最快的办法 :-)。

## 联系方式
有想说的联系：lm521299@sina.com

## 20190215log
* 修正使用leancloud时，生成报告时读取数据不全的问题。此bug只影响报告的生成，不影响数据爬取

## 20190123log
* 增加简单的数据比较功能
* 使用leancloud的需要添加masterkey参数到config.ini中

## 20200605log
* 增加报告上的房屋连接可以直接跳转

## 20201117log
* 修复链家数据错误的问题

![](https://img-blog.csdnimg.cn/20200715103658153.png)

# 希望发现不好用的时候邮件通知我一下，方便我尽快修改，谢谢 :-)
![](https://starchart.cc/tree-branch/house.svg)
↑看一下大家什么时候喜欢关注房源信息↑
