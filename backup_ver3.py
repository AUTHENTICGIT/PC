import os
import time
source = ['"C:\\Users\\xly\\Documents\\quiz04"', 'G:\Temp\hw']
target_dir = 'I:\\Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

comment = input('Enter a comment -->')
comment_list = comment.split(' ')
target = today + os.sep + time.strftime('%H%M%S'+'_'+'_'.join(comment_list)) + '.zip'
print(target)

if not os.path.exists(today):
    os.mkdir(today)
    print('Successful created directory', today)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))   # join用来连接字符串

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
