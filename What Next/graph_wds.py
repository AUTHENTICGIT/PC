# import matplotlib.pyplot as plt
# data = [1.5]*7 + [2.5]*2 + [3.5]*8 + [4.5]*3 + [5.5]*1 + [6.5]*8
# plt.hist(data, bins=6)
# plt.show()

import pymysql
import re
from numpy import mean, median
from collections import Counter
from matplotlib import pyplot

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

# 众数
def get_mode(arr):
    mode = []
    arr_appear = dict((a, arr.count(a)) for a in arr)  # 统计各个元素出现的次数
    if max(arr_appear.values()) == 1:  # 如果最大的出现为1
        return  # 则没有众数
    else:
        for k, v in arr_appear.items():  # 否则，出现次数最大的数字，就是众数
            if v == max(arr_appear.values()):
                mode.append(k)
    return mode

# table = input('请输入要计算的数据库表：')
conn = pymysql.Connect(host='localhost',
                       user='root',
                       passwd='1234',
                       db='wds',
                       charset='utf8mb4')
cur = conn.cursor()
# cur.execute("SELECT total_back_number from " + table)
cur.execute("SELECT total_back_number from userlist")
rows = cur.fetchall()
arr = []
for r in rows:
    item = float(re.findall(r".+'(.*)'.+", str(r))[0])
    arr.append(item)
# print(sorted(arr))
# print(len(arr))

print("极差为：{0:.2f}".format(Math.range(arr)))
print("平均数为：{0:.2f}".format(Math.avg(arr)))
print('中位数为：{0:.2f}'.format(get_median(arr)))
print('众数为：', get_mode(arr))

# 绘制散点图
def drawScatter(x, y):
    # 创建散点图
    # 第一个参数为点的横坐标
    # 第二个参数为点的纵坐标
    pyplot.scatter(x, y)
    pyplot.xlabel('Money')
    pyplot.ylabel('People')
    pyplot.title('Money & People Of ZY Wds')

# 统计每个金额重复出现的次数
count_times = dict(Counter(arr))
for k, v in count_times.items():
    if not k > 40000.00:
        money = k
        people = v
        drawScatter(money, people)

pyplot.show()
