import pymysql
import re
from collections import Counter
from matplotlib import pyplot
import time

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

# 求众数
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

# 绘制散点图
def drawScatter(x, y):
    # 创建散点图
    # 第一个参数为点的横坐标
    # 第二个参数为点的纵坐标
    pyplot.scatter(x, y)
    pyplot.xlabel('Money')
    pyplot.ylabel('People')
    pyplot.title('Money & People Of ZY Wds')

def main():
    try:
        table = input('请输入要计算的数据库表：')
    except EOFError:
        print('Why did you do an EOF on me?')
    except KeyboardInterrupt:
        print('You cancelled the operation.')
    else:
        # 将在没有异常发生时执行
        if table == 'userlist':
            print('\n切换到zy数据库表进行查询\n')
        elif table == 'mh':
            print('\n切换到mh数据库表进行查询\n')
        elif table == 'zyf':
            print('\n切换到zyf数据库表进行查询\n')
        elif table == 'watanabe':
            print('\n切换到watanabe数据库表进行查询\n')
        else:
            print('\n数据库不存在\n')

    conn = pymysql.Connect(host='localhost',
                           user='root',
                           passwd='1234',
                           db='wds',
                           charset='utf8mb4')
    cur = conn.cursor()
    cur.execute("SELECT total_back_number from " + table)
    rows = cur.fetchall()
    arr = []
    for r in rows:
        item = float(re.findall(r".+'(.*)'.+", str(r))[0])
        arr.append(item)

    print("极差为：{0:.2f}".format(Math.range(arr)))
    print("平均数为：{0:.2f}".format(Math.avg(arr)))
    print('中位数为：{0:.2f}'.format(get_median(arr)))
    print('众数为：', get_mode(arr))
    print('\n')

    # 统计每个金额重复出现的次数
    count_times = dict(Counter(arr))
    for k, v in count_times.items():
        if not k > 40000.00:
            money = k
            people = v
            drawScatter(money, people)
    print('散点图正在绘制中...稍后呈现...')
    time.sleep(1)
    pyplot.show()

if __name__ == '__main__':
    main()