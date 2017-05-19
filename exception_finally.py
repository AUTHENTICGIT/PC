# import sys
# import time
#
# try:
#     fhand = open('C:/Users/xly/Desktop\poem.txt')
#     for line in fhand:
#         print(line, end='')
#         print('Press ctrl+c now')
#         time.sleep(2)
# except IOError:
#     print('Could not find file poem.txt')
# except KeyboardInterrupt:
#     print('!! You canceled the reading from the file.')
# finally:
#     if fhand:
#         fhand.close()
#     print('(Cleaning up: Closed the file)')

# 案例

# 案例
import sys
import time

f = None
try:
    f = open("C:/Users/xly/Desktop\poem.txt")
    # 我们常用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end = '')
        sys.stdout.flush()  # Linux系统下，必须加入sys.stdout.flush()才能一秒输一个数字；Windows系统下，加不加都能
        print('Press ctrl+c now')
        # 为了确保它运行一段时间
        time.sleep(2)
except IOError:
    print('Could not find the poem.txt')
except KeyboardInterrupt:
    print('!! You canceled the reading from the file.')
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
