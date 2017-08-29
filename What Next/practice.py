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
import urllib.parse
from bs4 import BeautifulSoup
import re


def gethomelink(keyword):
    url = "http://tieba.baidu.com/f?kw=" + urllib.parse.quote(keyword)
    return url


def getlinklist(inputlink):  # 这个函数是获取一个页面上所有帖子的链接
    pages = []  # 一个列表
    html = urllib.request.urlopen(inputlink)
    bsobj = BeautifulSoup(html, "html.parser")
    titlelist = bsobj.findAll("a", {"class": "j_th_tit "})
    for title in titlelist:
        pages.append("http://tieba.baidu.com" + title.attrs["href"])
    return pages


def same(page1, page2):
    pages1 = []
    pages2 = []
    html1 = urllib.request.urlopen(page1)
    bsobj1 = BeautifulSoup(html1, "html.parser")
    titlelist = bsobj1.findAll("a", {"class": "j_th_tit "})
    for title in titlelist:
        pages1.append(title.get_text())

    html2 = urllib.request.urlopen(page2)
    bsobj2 = BeautifulSoup(html2, "html.parser")
    titlelist2 = bsobj2.findAll("a", {"class": "j_th_tit "})
    for title in titlelist2:
        pages2.append(title.get_text())
    same = 0
    if pages1 == pages2:
        same = 1
    else:
        same = 0
    return same


def getcontent(url):
    try:
        html = urllib.request.urlopen(url)
        html = html.read().decode('utf-8', 'ignore')
        title = re.findall(r'title:".*?"|title: ".*?"', html)
        title = re.findall(r'".*"', title[0])
        bsobj = BeautifulSoup(html, "html.parser")
        content = bsobj.find("div", {"class": re.compile(
            "(d_post_content j_d_post_content )|(d_post_content j_d_post_content  clearfix)")})
        print("《", title[0][1:-1], "》")
        print(content.get_text()[8:-1])
    except UnicodeEncodeError as reason:
        print("遇到非法内容，可能含有未能识别编码！程序结束！")


def allpagelink(keyword, yourwantnumber):  # 获取所有页面的所有的帖子连接
    number = int(yourwantnumber)
    wantnumber = number * 50
    url = gethomelink(keyword)
    endpageurl = url + "&pn=10000"
    linklist = list()
    pagenumber = 0
    stop = 0
    while stop == 0:
        thispageurl = url + "&pn=" + str(pagenumber)
        linklist.extend(getlinklist(thispageurl))
        pagenumber += 50
        wantnumber -= 50
        if same(thispageurl, endpageurl) == 1:
            stop = 1
        elif wantnumber <= 0:
            stop = 1

    return linklist


def main():
    try:
        wantnumber = 1.0
        print("""#贴吧爬虫v1.0#
##输入正确的贴吧名称和爬取页数即可爬取每个帖子的标题和一楼内容##
##爬取过程中按Ctrl+C可结束程序##\n""")
        keyword = input("->请输入一个正确的贴吧名称：")

        wantnumber = input("->你想获取几页内容（1~10000）？")
        wantnumber = int(float(wantnumber))
        linkset = allpagelink(keyword, wantnumber)
        for link in linkset:
            getcontent(link)
    except ValueError as reason:
        print("输入页数非法！程序结束。")
    except KeyboardInterrupt as reason:
        print("程序结束！")


if __name__ == "__main__":
    main()