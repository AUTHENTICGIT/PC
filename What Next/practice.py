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
import re
from bs4 import BeautifulSoup
# 获得所有帖子地址列表，返回第一个帖子地址
def getLinkList(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    # 找标题
    homepage_titles = soup.find_all('a', class_ = 'j_th_tit')
    soup.a.text
    # print(homepage_titles)
    # 取标题中对应地址
    href_list = []
    title_list = []
    for href in homepage_titles:
        # print(href)
        item = re.findall(r'/p/\d+', str(href))
        href_list.append(item[0])
    for title in homepage_titles:
        item = re.findall(r'<a.*? title="(.*?)".*?>.*?</a>', str(title))
        title_list.append(item[0])
    return (title_list, href_list)


inputlink = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E4%B8%AA%E5%A5%B3%E5%AD%A9&ie=utf-8'
title, title_add = getLinkList(inputlink)
print(title)
print(title_add)
