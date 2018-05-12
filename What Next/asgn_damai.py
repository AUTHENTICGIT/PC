"""
Created on Sat May 12 18:45:46 2018

@author: AUT
"""

import requests
import time

def search(FromData):
    searchCount = 0
    while(True):
        r = requests.post('https://search.damai.cn/searchajax.html', data=FromData,)
        result = r.text
        result= eval(result)   # 把str类型，转换为字典类型
        # print(result)
        pageData = result['pageData']

        if pageData.__contains__('resultData') & pageData['totalResults']>0:
            print(pageData['resultData'])
            break
        else:
            searchCount += 1
            print(format(searchCount))
            time.sleep(5)

        # 加头反爬
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # req = urllib.request.Request(url='https://search.damai.cn/search.html', headers=headers)

def main():
    data = {
        "keyword": "SNH48 成都"
    }
    search(data)

if __name__ == "__main__":
    main()