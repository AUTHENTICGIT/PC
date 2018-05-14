"""
Created on Sat May 12 18:45:46 2018

@author: AUT
"""

import requests
import time
import itchat

def search(FromData):
    searchCount = 0

    #登陆微信,记住登陆状态
    itchat.auto_login(hotReload=True)

    # 获取微信名
    users = itchat.search_friends('Admin')
    wxname = (users[0]['UserName'])

    while(True):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        r = requests.post('https://search.damai.cn/searchajax.html', data=FromData, headers=headers)
        print(r)
        result = r.text
        result= eval(result)   # 把str类型，转换为字典类型
        # print(result)
        pageData = result['pageData']
        if pageData.__contains__('resultData') & pageData['totalResults']>0:
            print(pageData['resultData'])
            itchat.send('有新票务更新！！！', toUserName=wxname)
            itchat.send_msg(str(pageData['resultData']), toUserName=wxname)
            break
        else:
            searchCount += 1

            print(searchCount, time.asctime(time.localtime(time.time())))
            time.sleep(30)

def main():
    data = {
        "keyword": "SNH48 成都"
    }
    search(data)

if __name__ == "__main__":
    main()
