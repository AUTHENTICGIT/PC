from time import ctime
from bs4 import BeautifulSoup
import itchat
import urllib.request
from pandas import Series

@itchat.msg_register(itchat.content.TEXT)
def getcity(msg):
    print(msg["Text"])
    pinyin = msg['Text']
    results = getTour(pinyin)
    itchat.send(results, msg['FromUserName'])

# 登录网页版微信
itchat.login()
Help = """友情提示：
请输入经典拼音获取经典信息
注意：
陕西——请输入shaanxi
吉林市——请输入jilinshi
抚州请输入——jiangxifuzhou
"""
itchat.send(Help, toUserName='filehelper')

urllib.request.urlopen('https://lvyou.baidu.com')
