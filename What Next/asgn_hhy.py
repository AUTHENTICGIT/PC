import urllib.request
from bs4 import BeautifulSoup
import re
from lxml import etree

# 获得贴吧地址，并返回
def getHomeLink(keyword):
    url = 'http://tieba.baidu.com/f?kw=' + urllib.parse.quote(keyword)
    return url

# 获得所有帖子地址列表，并返回所有帖子地址
def getLinkList(keyword, page):
    title_list = []
    href_list = []
    for i in range(page):
        inputlink = getHomeLink(keyword) + '&ie=utf-8&pn=' + str(i*50)
        response = urllib.request.urlopen(inputlink)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        # 找标题
        homepage_titles = soup.find_all('a', class_ = 'j_th_tit')
        # print(homepage_titles)
        # 取标题中对应地址
        for href in homepage_titles:
            # print(href)
            item = re.findall(r'/p/\d+', str(href))
            href_list.append(item[0])
        # print(href_list)
        # url = 'http://tieba.baidu.com' + href_list[0]
        for href in homepage_titles:
            item = re.findall(r'<a.*? title="(.*?)".*?>.*?</a>', str(href))
            title_list.append(item[0])
    return(title_list, href_list)

# 获得每层内容
def getContent(url, page):
    try:
        content_list = []
        for i in range(page):
            response = urllib.request.urlopen(url+str(i+1))
            html = response.read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            # print(soup)
            page_content_list = soup.find_all('div', {"class": re.compile("(d_post_content j_d_post_content )|(d_post_content j_d_post_content  clearfix)")})
            # print(page_content_list)
            for item in page_content_list:
                content = item.get_text()[8:]
                content_list.append(content)
        for i in range(len(content_list)):
            print('['+ str(i+1) +'L]', content_list[i])
        # print(content_list)
    except UnicodeEncodeError as reason:
        print('遇到非法内容，可能含有未能识别编码！程序结束！')

def main():
    try:
        keyword = input('->请输入一个正确的贴吧名称：')
        wantnumber = int(input('->你想获取几页内容（1~10000）？'))
        if keyword == '1':
            keyword = '生个女孩'
        elif keyword == '2':
            keyword = '塞纳河路边社'
        print('->正在前往' + keyword + '吧......')
        title, title_list = getLinkList(keyword, wantnumber)
        for i in range(wantnumber*50):
            name = title[i]
            url = 'http://tieba.baidu.com' + title_list[i]
            print(i+1, name, url)
        # getContent('http://tieba.baidu.com' + title_list[0])
        inp_no = input('->请输入要查看帖子的编号：')
        inp_page = int(input('->请输入要查看《' + title[int(inp_no)-1] + '》的页数：'))
        tie_url = 'http://tieba.baidu.com' + title_list[int(inp_no)-1] + '?pn='
        getContent(tie_url, inp_page)
        input('Press Enter to exit...')
    except KeyboardInterrupt as reason:
        print('程序结束！')

if __name__ == "__main__":
    main()
