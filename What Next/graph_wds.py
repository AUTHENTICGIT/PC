# import matplotlib.pyplot as plt
# data = [1.5]*7 + [2.5]*2 + [3.5]*8 + [4.5]*3 + [5.5]*1 + [6.5]*8
# plt.hist(data, bins=6)
# plt.show()

import pymysql
import re
import time
import random

class Math:
    # 求极差
    @staticmethod
    def range(l):
        return max(l) - min(l)

    # 求平均数
    @staticmethod
    def avg(l):
        return float(sum(l)) / len(l)
# 求中位数
def get_median(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2

conn = pymysql.Connect(host='localhost',
                       user='root',
                       passwd='1234',
                       db='wds',
                       charset='utf8mb4')
cur = conn.cursor()
cur.execute("SELECT total_back_number from userlist")
rows = cur.fetchall()
arr = []
for r in rows:
    item = float(re.findall(r".+'(.*)'.+", str(r))[0])
    arr.append(item)
# print(sorted(arr))
# print(len(arr))

print("极差为：{0}".format(Math.range(arr)))
print("平均数为：{0:.2f}".format(Math.avg(arr)))
print('中位数为：{0:.2f}'.format(get_median(arr)))
