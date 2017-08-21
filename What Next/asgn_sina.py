import urllib.request

# 分析网页函数
def fetch_weibo():
    api = 'http://m.weibo.cn/index/my?format=cards&page=%s'
    cookies = 'Cookie:SINAGLOBAL=9974812462855.709.1502431721003; UM_distinctid=15def82f1872d0-04f83542c353fe-791238-1fa400-15def82f188c2e; UOR=,,www.baidu.com; login_sid_t=52ed1f4085942a94fcb379ba8a49663a; _s_tentry=-; Apache=7526552271580.26.1503293383624; ULV=1503293383629:4:4:1:7526552271580.26.1503293383624:1502961922922; SCF=AoTUoNJygLXGxCh5kwCRSHBhIHW2kkPizeX0rEoD73GH13j8A7j28pUOIWyTR1nxVi-4KVKynzy1VcmakEULQEU.; SUB=_2A250ngGPDeRhGeNN6FIX-C7OzTmIHXVX6nRHrDV8PUJbmtBeLXPukW9fTHO3vyAfsfHLOWHxIXnZwF2Gmg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW5jLW.fpWA1aAWiMjrTo735JpX5K2hUgL.Fo-0e05c1h5ESo-2dJLoIEBLxK-L1-qL12-LxK-L1h-LBKMLxK-LB-BLBonLxK.L1K-LBoMt; SUHB=0tKanWpEtqjyBX; SSOLoginState=1503293919; un=leogwork@gmail.com; wvr=6'
    for i in range(1,102):
        response = urllib.request.get(url = api % i, cookies=cookies)
        data = response.json()[0]
        groups = data.get('card_group') or []
        for group in groups:
            text = group.get('mblog').get('text')
            text = text.encode('utf-8')
            text = cleanring(text).strip()
            yield text