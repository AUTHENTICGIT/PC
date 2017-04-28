# # zip打包命令 zip [参数] [打包后的文件名] [打包的目录路径]
# # 获取当前时间可以用time包strftime()函数
# # os.system()执行系统命令，运行成功将返回0，运行失败将返回错误代码
# import os
# import time
#
# # 备份的目录
# source = 'C:\\Users\\xly\\Documents\\quiz04'
# print(os.listdir(source))
# # 备份到主目录
# target_dir = 'I:\\Backup'
#
# # zip压缩文件的文件名由当前日期与时间构成
# target_name = time.strftime('%Y%m%d%H%M%S') + '.zip'    # strftime()函数可以将时间根据传入的模板格式化时间字符串
#
# # 备份文件将打包压缩成zip文件
# target = target_dir + os.sep + target_name  # os.sep会根据你的操作系统给出响应的分隔符，在Windows中是'\\'，在Unix中是'/'，在MacOS中是':'
#
# # 用zip命令将文件打包成zip格式
# zip_command = 'zip -r {} {}'.format(target, source)
#
# # 如果目录不存在，进行创建
# if not os.path.exists(target_dir):
#     os.mkdir(target_dir)
#
# #执行备份
# print('Zip command:')
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

#2. 备份文件必须存储在一个
#主备份目录中
# 例如在 Mac OS X 和 Linux 下：
# target_dir = '/Users/swa/backup'
# 又例如在 Windows 下：
target_dir = 'I:\\Backup'

# 3. 备份文件将打包压缩成 zip 文件。
# 4. zip 压缩文件的文件名由当前日期与时间构成。
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5. 我们使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))   # join用来连接字符串

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target_dir)
else:
    print('Backup FAILED')
