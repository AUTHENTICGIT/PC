import requests

'''
https://zhongchou.modian.com/realtime/ajax_dialog_user_list?jsonpcallback=jQuery1111012182719838104772_1526554153521&origin_id=16056&type=backer_list&page=1&page_size=20&cate=2&_=1526554153523

window[decodeURIComponent('jQuery1111012182719838104772_1526554153521')]({"html":"\n<div class=\"wds_banner\">\n
    <div class=\"tab\">\n
        <span data-cate=\"2\" class=\"active\">\u805a\u805a\u699c<i class=\"s_icon\"><\/i><\/span>\n
        <span data-cate=\"1\">\u6253\u5361\u699c<i class=\"s_icon\"><\/i><\/span>\n    
        <\/div>\n    
        <\/div>\n<ul class=\"wds_like_ul\">\n            
        <li class=\"wds_item first\">\n      //第一      
          <div class=\"no\"><\/div>\n            
          <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=985962&amp;_mpos=pro_backer_web\">\n                
            <img src=\"https:\/\/tva2.sinaimg.cn\/crop.0.0.996.996.180\/7ed866ecjw8f9im8fkpwlj20ro0romz1.jpg\" 
            alt=\"\" 
            onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            
          <\/div>\n            
          <div class=\"item_cont\">\n                
            <p>\u6708\u66ae\u79e6\u5173<\/p>\n                
            <p>\u00a51,674<\/p>\n            
          <\/div>\n        
        <\/li>\n            
        <li class=\"wds_item second\">\n     //第二       
          <div class=\"no\"><\/div>\n            
          <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=986166&amp;_mpos=pro_backer_web\">\n                
          <img src=\"https:\/\/p.moimg.net\/ico\/986166_1495726264.jpg\" 
            alt=\"\" 
            onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            
          <\/div>\n            
          <div class=\"item_cont\">\n                
            <p>joeqiang<\/p>\n                
            <p>\u00a51,294<\/p>\n            
          <\/div>\n        
        <\/li>\n            
        <li class=\"wds_item third\">\n    //第三        
          <div class=\"no\"><\/div>\n            
          <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1442771&amp;_mpos=pro_backer_web\">\n                
            <img src=\"https:\/\/u.moimg.net\/ico\/1442771_1499254858.jpg\" //图片
            alt=\"\" 
            onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            
          <\/div>\n            
          <div class=\"item_cont\">\n                
            <p>\u7ea2\u7ef3\u4f1a\u5bb6\u9171\u6cb9\u7684<\/p>\n                
            <p>\u00a51,118.1<\/p>\n      //金额      
          <\/div>\n        
        <\/li>\n            
        <li class=\"wds_item\">\n            
          <div class=\"no\">4<\/div>\n            
          <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1194671&amp;_mpos=pro_backer_web\">\n                
            <img src=\"https:\/\/u.moimg.net\/ico\/1194671_1510396910.jpg\" 
            alt=\"\" 
            onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            
          <\/div>\n            
          <div class=\"item_cont\">\n                
            <p>Mu\u77e2<\/p>\n                
            <p>\u00a5858<\/p>\n            
          <\/div>\n        
        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">5<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1104581&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/u.moimg.net\/ico\/1104581_1505312904.jpg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            
        <div class=\"item_cont\">\n                <p>\u4e00\u53ea\u559c\u6b22\u8d75\u7ca4\u7684\u732b<\/p>\n                
        <p>\u00a5705<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">6<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1446618&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/p.moimg.net\/ico\/2018\/05\/13\/20180513_1526185602_1848.jpg?imageMogr2\/auto-orient\/strip\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            
        <div class=\"item_cont\">\n                <p>\u718a\u732b_Nick<\/p>\n                
        <p>\u00a5620<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">7<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=989346&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/p.moimg.net\/icon\/2015\/06\/03\/989346_1493178863.jpeg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>\u8179\u9ed1\u5f88\u60f3\u5ff5<\/p>\n                
        <p>\u00a5605<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">8<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1432580&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/p.moimg.net\/ico\/2018\/04\/06\/20180406_1522945064_3821.jpg?imageMogr2\/auto-orient\/strip\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>\u5c0f\u6bd2\u836f<\/p>\n                
        <p>\u00a5529<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">9<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1285934&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/u.moimg.net\/ico\/1285934_1496837216.jpg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>\u8fdc\u5f26<\/p>\n                
        <p>\u00a5520<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">10<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1067405&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/u.moimg.net\/ico\/1067405_1506475268.jpg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>\u51cc\u8f69\u5e94\u63f4\u4f1a<\/p>\n                
        <p>\u00a5515<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">11<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1271241&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/u.moimg.net\/ico\/1271241_1504269735.jpg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>\u82b1\u80e1\u841d\u535c\u6a58\u5b50\u65d7<\/p>\n                
        <p>\u00a5509<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">12<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1542532&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/p.moimg.net\/ico\/2018\/02\/11\/20180211_1518338087_4422.jpg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>\u5c0f\u98de\u7684\u554a\u6148<\/p>\n                
        <p>\u00a5470<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">13<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1283085&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/p.moimg.net\/ico\/2018\/01\/21\/20180121_1516541589_1196.jpg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>LXH_<\/p>\n                
        <p>\u00a5435<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">14<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1170385&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/p.moimg.net\/ico\/2018\/05\/08\/20180508_1525733256_8292.jpg?imageMogr2\/auto-orient\/strip\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>QDVBRCHY<\/p>\n                
        <p>\u00a5430.8<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">15<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1087423&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/u.moimg.net\/ico\/1087423_1499255248.jpg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>\u5bd2\u6c5f\u6709\u6c5c<\/p>\n                
        <p>\u00a5429<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">16<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1418213&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/p.moimg.net\/ico\/2018\/03\/01\/20180301_1519908469_1039.jpg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>\u5de7\u514b\u529b\u6f02\u6d6e<\/p>\n                
        <p>\u00a5405<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">17<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1251902&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/p.moimg.net\/ico\/2018\/03\/12\/20180312_1520868081_2831.jpg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>\u7ea2\u7ef3\u4f1a\u7684\u5c0f\u5f1f<\/p>\n                
        <p>\u00a5377.28<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">18<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1067949&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/tva1.sinaimg.cn\/crop.0.1.750.750.180\/006stD0ajw8f42d2xyd0xj30ku0kwq45.jpg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>\u5355\u63a8\u8d75\u7ca4\u7684pqE<\/p>\n                
        <p>\u00a5375<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">19<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=1459761&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/p.moimg.net\/icon\/2017\/07\/17\/1459761_1500293231.jpeg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>Bowen<\/p>\n                
        <p>\u00a5350<\/p>\n            <\/div>\n        <\/li>\n            
        <li class=\"wds_item\">\n            <div class=\"no\">20<\/div>\n            <div class=\"item_logo\" data-href=\"https:\/\/me.modian.com\/u\/detail?uid=19796&amp;_mpos=pro_backer_web\">\n                <img src=\"https:\/\/p.moimg.net\/ico\/19796_1485701475.jpg\" alt=\"\" onerror=\"javascript:this.src='https:\/\/s.moimg.net\/img\/web4-0\/default_profile@3x.png'\">\n            <\/div>\n            <div class=\"item_cont\">\n                <p>35\u63a5\u529b500\u68d2\u8ddf\u6295<\/p>\n                
        <p>\u00a5330.8<\/p>\n            <\/div>\n        <\/li>\n    <\/ul>","title":"\u652f\u6301\u8005 300"});
'''

def getQueryString():
    QueryString = {
        'jsonpcallback': 'jQuery111105399095815167287_1526554345136',
        'origin_id':16056,
        'type':'backer_list',
        'page':1,
        'page_size':100,
        '_':1526554345145
    }
    return QueryString

def main():
    pass

if __name__ == '__main__':
    main()