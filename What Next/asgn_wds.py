import requests
import pymysql

def getFromData(pro_id, num):
    FromData = {
        'pro_id':pro_id,
        'type':1,
        'page':1,
        'pageSize':num
    }
    return FromData

def getUserList(id, num):
    # 模拟发POST请求，并获得返回的json数据
    FromData = getFromData(id, num)
    r = requests.post('https://wds.modian.com/ajax_backer_list', data = FromData)
    user = r.text
    user = eval(user)   # 返回的数据实际是str类型，要转换为字典类型
    user_list = user['data']
    print(user_list)

def main():
    url = 'https://wds.modian.com/ranking_list?pro_id=6195'
    pro_id = 6195
    num = int(input('Enter Numbers:'))
    getUserList(pro_id, num)

if __name__ == "__main__":
    main()