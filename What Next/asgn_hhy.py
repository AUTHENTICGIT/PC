import urllib.request
from bs4 import BeautifulSoup
import re
from lxml import etree

def getHomeLink(keyword):
    url = 'http://tieba.baidu.com/f?kw=' + urllib.parse.quote(keyword)
    return url

def getLinkList(inputlink):
    response = urllib.request.urlopen(inputlink)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    # 找标题
    homepage_titles = soup.find_all('a', class_ = 'j_th_tit')
    # print(homepage_titles)
    # 取标题中对应地址
    href_list = []
    for href in homepage_titles:
        # print(href)
        item = re.findall(r'/p/\d+', str(href))
        href_list.append(item[0])
    # print(href_list)

    url = 'http://tieba.baidu.com' + href_list[0]

def getContent(url):
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        page_contents_list = soup.find_all('div', {"class": re.compile("(d_post_content j_d_post_content )|(d_post_content j_d_post_content  clearfix)")})
        print(page_contents_list)
    except UnicodeEncodeError as reason:
        print('遇到非法内容，可能含有未能识别编码！程序结束！')

def main():
    try:
        keyword = input('->请输入一个正确的贴吧名称：')
