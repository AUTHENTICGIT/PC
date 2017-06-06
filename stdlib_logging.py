import platform
import os
import logging

if platform.platform().startswith('Windows'):   # platform.platform()获取操作系统名称及版本号
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), # os.getenv()读取环境变量
                                os.getenv('HOMEPATH'),
                                'test.log')
    print(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'))
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print('Logging to', logging_file)

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
)

logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')

import os

print(os.getenv('HOMEDRIVE'))
print(os.getenv('USERNAME'))
print(os.getenv('HOMEPATH'))
print(os.getenv('PYTHONPATH'))
