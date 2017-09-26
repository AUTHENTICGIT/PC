import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; L50t Build/17.1.E.2.67; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN'
    }
cookies = {
    'PHPSESSID':'b75nd30mutioeqp2ep5g133on2',
    'Hm_lvt_d703449a63eadad220b77508bbd3b2f6':'1505881642',
    'Hm_lpvt_d703449a63eadad220b77508bbd3b2f6':'1506064461'
}
data = {'cmd':'vote', 'uid':'7'}
page1 = 'http://www.yindudigital.cn/zj/20170825/?from=singlemessage'
page2 = 'http://www.yindudigital.cn/zj/cache/wx_config.php'
vote = 'http://www.yindudigital.cn/zj/20170825/api.php'
r = requests.post(url=vote, headers=headers, cookies=cookies, data=data)
html = r.text
print(html)