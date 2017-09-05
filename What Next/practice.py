# import urllib.request
# import re
#
# # 全部PNG
# request = urllib.request.urlopen('http://www.baidu.com')
# resource = request.read().decode()  # read获取的类型为bytes，用encode()解码成str
# print(re.findall('http://.+\.png' ,resource))

from selenium import webdriver
import time
from bs4 import BeautifulSoup

# # 用IEDriver方式打开wds页面
# browser = webdriver.Ie()
# browser.get("https://wds.modian.com/ranking_list?pro_id=5901")

driver = webdriver.Chrome()     # 用chrome浏览器打开
driver.get('https://wds.modian.com/ranking_list?pro_id=5901')       # 打开wds页面
time.sleep(2)       # 让操作稍微停一下

# 定义一个函数，实现将滚轮滑到页面最下方的功能，每5s下移一次，一共下移10次
def execute_times(times):
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
execute_times(2)

html=driver.page_source
print(html)

