# file = input('Enter file name:')
# try:
#     fhand = open(file)
# except:
#     print('File not exist!')
# for line in fhand:
#     print(line, end = '')

# 案例
try:
    # 一般会把通常的语句放在try代码块中
    text = input('Enter something --->')
except EOFError:
    # 把错误处理器代码放在except代码块中
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    # 将在没有异常发生时执行
    print('You entered {}'.format(text))
