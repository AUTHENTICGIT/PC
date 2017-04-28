# import os
# import time
# source = ['C:\\Users\\xly\\Documents\\quiz04', 'G:\Temp\hw']
# target_dir = 'I:\\Backup'
# target = target_dir + os.sep + time.strftime('%Y%m%d') + os.sep + time.strftime('%H%M%S') + '.zip'
#
# if not os.path.exists(target_dir + os.sep + time.strftime('%Y%m%d')):
#     os.mkdir(target_dir + os.sep + time.strftime('%Y%m%d'))
#
# zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
#
# print('Zip command is:')
# print(zip_command)
# print('Running:')
# if os.system(zip_command) == 0:
#     print('Successful backup to', target)
# else:
#     print('Backup FAILED')

# 案例
import os
import time

# 1. 需要备份的文件与目录将被
# 指定在一个列表中。
# 例如在 Mac OS X 与 Linux 下：
# source = ['/Users/swa/notes']
# 又例如在 Windows 下：
source = ['"C:\\Users\\xly\\Documents\\quiz04"', 'G:\Temp\hw']
# 在这里要注意到我们必须在字符串中使用双引号
# 用以括起其中包含空格的名称。

# 2. 备份文件必须存储在一个
# 主备份目录中
# 例如在 Mac OS X 和 Linux 下：
# target_dir = '/Users/swa/backup'
# 又例如在 Windows 下：
target_dir = 'I:\\Backup'

# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 3. 备份文件将打包压缩成 zip 文件。
# 4. 将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')

# zip 文件名称格式
target = today + os.sep + time.strftime('%H%M%S')

# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successful created directory', today)

# 5. 我们使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))   # join用来连接字符串

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
