import urllib.request
from bs4 import BeautifulSoup
import re
from lxml import etree

# 获得贴吧地址，并返回
def getHomeLink(keyword):
    url = 'http://tieba.baidu.com/f?kw=' + urllib.parse.quote(keyword)
    return url

# 获得所有帖子地址列表，返回第一个帖子地址
def getLinkList(keyword):
    inputlink = getHomeLink(keyword)
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
    # url = 'http://tieba.baidu.com' + href_list[0]
    title_list = []
    for href in homepage_titles:
        item = re.findall(r'<a.*? title="(.*?)".*?>.*?</a>', str(href))
        title_list.append(item[0])
    return(title_list, href_list)

# 获得每层内容
def getContent(url):
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        page_content_list = soup.find_all('div', {"class": re.compile("(d_post_content j_d_post_content )|(d_post_content j_d_post_content  clearfix)")})
        print(page_content_list)
        content_list = []
        for item in page_content_list:
            content = re.findall(r'<div class="d_post_content j_d_post_content clearfix".*>(.*)</div>', item)
            content_list.append(content)
        print(content_list)
    except UnicodeEncodeError as reason:
        print('遇到非法内容，可能含有未能识别编码！程序结束！')

def main():
    try:
        keyword = input('->请输入一个正确的贴吧名称：')
        title, title_list = getLinkList(keyword)
        for i in range(20):
            name = title[i]
            url = 'http://tieba.baidu.com' + title_list[i]
            print(name, url)
        getContent('http://tieba.baidu.com' + title_list[0])
    except KeyboardInterrupt as reason:
        print('程序结束！')

if __name__ == "__main__":
    main()
