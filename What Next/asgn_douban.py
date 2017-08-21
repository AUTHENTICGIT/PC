import urllib.request
from bs4 import BeautifulSoup
import re
import jieba
import pandas
import numpy

response1 = urllib.request.urlopen("https://movie.douban.com/cinema/nowplaying/chengdu/")
html_data1 = response1.read().decode('utf-8')

soup1 = BeautifulSoup(html_data1, 'html.parser')

# find_all()搜索想要查找的内容，如div标签，标签id值为nowplaying
nowplaying_movie = soup1.find_all('div', id="nowplaying")
# find_all()返回结果为列表list，查找内容在列表第1个元素[0]，如在nowplay_movie[0]中查找class类
nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_ = 'list-item')

nowplaying_list = []
for item in nowplaying_movie_list:
    nowplaying_dict = {}
    nowplaying_dict['id'] = item['data-subject']
    nowplaying_dict['name'] = item['data-title']
    nowplaying_list.append(nowplaying_dict)

response2 = urllib.request.urlopen('https://movie.douban.com/subject/' + nowplaying_list[0]['id'] + '/comments?')
html_data2 = response2.read().decode('utf-8')
soup2 = BeautifulSoup(html_data2, 'html.parser')
comment_div_list = soup2.find_all('div', class_ = 'comment')

eachCommentList = []
for item in comment_div_list:
    if item.find('p').string is not None:   # item.find('p').string 查找p标签中的字符串
        eachCommentList.append(item.find('p').string)

# 数据清洗
comments = ''
for k in range(len(eachCommentList)):
    comments = comments + (str(eachCommentList[k])).strip() # strip()移除字符串首尾

# 将匹配中文的正则表达式编译为pattern对象，供findall()和search()等函数使用
pattern = re.compile(r'[\u4e00-\u9fa5]+')
# findall()查找得到list
filterdata = re.findall(pattern, comments)
# ''.join()把list中各元素连接为字符串
cleaned_comments = ''.join(filterdata)

# 词频统计
# 用结巴分词做中文分词，lcut()返回分词list
segment = jieba.lcut(cleaned_comments)
# 用pandas，DataFrame表格数据结构
words_df = pandas.DataFrame({'segment': segment})
# 去掉停用词
stopwords = pandas.read_csv('F:\stopwords.txt', index_col=False, sep='\t', names=['stopword'], encoding='utf-8')
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

# 词频统计
words_stat = words_df.groupby(by=['segment'])['segment'].agg({'计数':numpy.size})
words_stat = words_stat.reset_index().sort_values(by=['计数'],ascending=False)
print(words_stat.head())