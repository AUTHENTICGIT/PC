import re
import os
# -*- coding: gbk -*-

def get_idCard():
    path = "/Users/learnlearn/Desktop/ss" #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    s = []
    for file in files: #遍历文件夹
         if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
              f = open(path+"/"+file) #打开文件
              iter_f = iter(f) #创建迭代器
              str = ""
              for line in iter_f: #遍历文件，一行行遍历，读取文本
                  str = str + line
              s.append(str) #每个文件的文本存到list中
    print(s) #打印结果
    count = 0
    for item in s:
        id_list = re.findall(r'\d{18}', item)
        count = count + len(id_list)
    return count

def get_idCard2():
    path = "/Users/learnlearn/Desktop/ss/sale to  aaafols  201703-05.txt"
    f = open(path, encoding='gbk')
    count = 0
    for line in f:
        print(line)
        if re.search(r'\d{18}', line) != -1:
            count = count + 1
        print(count)
    return count

def main():
    # count = get_idCard()
    # print(count)
    get_idCard2()

if __name__ == '__main__':
    main()

