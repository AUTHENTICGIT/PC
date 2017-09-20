import urllib.request
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

html = 'https://wds.modian.com/show_weidashang_pro/6195#1'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=html, headers=headers)
html_data = urllib.request.urlopen(req).read().decode('utf8')
print(html_data)

from matplotlib import pyplot

def drawScatter(x, y):
    # 创建散点图
    # 第一个参数为点的横坐标
    # 第二个参数为点的纵坐标
    pyplot.scatter(x, y)
    pyplot.xlabel('Money')
    pyplot.ylabel('People')
    pyplot.title('Money & People Of ZY Wds')
drawScatter(1.66, 2)
drawScatter(2.66, 10)

pyplot.show()