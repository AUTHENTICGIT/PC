# # import urllib.request
# # import re
# #
# # # 全部PNG
# # request = urllib.request.urlopen('http://www.baidu.com')
# # resource = request.read().decode()  # read获取的类型为bytes，用encode()解码成str
# # print(re.findall('http://.+\.png' ,resource))
#
# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup
#
# # # 用IEDriver方式打开wds页面
# # browser = webdriver.Ie()
# # browser.get("https://wds.modian.com/ranking_list?pro_id=5901")
#
# driver = webdriver.Chrome()     # 用chrome浏览器打开
# driver.get('https://wds.modian.com/ranking_list?pro_id=5901')       # 打开wds页面
# time.sleep(2)       # 让操作稍微停一下
#
# # 定义一个函数，实现将滚轮滑到页面最下方的功能，每5s下移一次，一共下移10次
# def execute_times(times):
#     for i in range(times + 1):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)
# execute_times(2)
#
# html=driver.page_source
# print(html)

import urllib.request
from bs4 import BeautifulSoup
import re
import pymysql

conn = pymysql.Connect(host='localhost', user='root', passwd='', db='wds', charset='utf8')
cur = conn.cursor()
sql = 'INSERT INTO userlist values(%s, %s, %s, %s, %s)'

# 单行插入
# userlist = ['1442771', 37867.77, '酱油', 'https:\\/\\/u.moimg.net\\/ico\\/1442771_1499254858.jpg', 'https:\\/\\/s.moimg.net\\/new_wds\\/images\\/default-avatar.png']
# data = tuple(userlist)
# print(data)
# cur.execute(sql % data)

# 批量插入
table = [
    ('1442771', 37867.77, '红绳会家酱油的', 'https:\\/\\/u.moimg.net\\/ico\\/1442771_1499254858.jpg', 'https:\\/\\/s.moimg.net\\/new_wds\\/images\\/default-avatar.png'),
    ('1137032', 23107.5, '恩兔恩兔Tanyc', 'https:\\/\\/p.moimg.net\\/ico\\/1137032_20170503_1493802333_4868.jpg', 'https:\\/\\/s.moimg.net\\/new_wds\\/images\\/default-avatar.png'),
    ('1104581', 18435.54, '一只喜欢赵粤的猫', 'https:\\/\\/u.moimg.net\\/ico\\/1104581_1504268125.jpg', 'https:\\/\\/s.moimg.net\\/new_wds\\/images\\/default-avatar.png'),
]

cur.executemany(sql, table)

conn.commit()
cur.close()
conn.close()

