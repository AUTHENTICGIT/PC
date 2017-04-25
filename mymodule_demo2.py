# 案例
# from mymodule import say_hi, __version__
#
# say_hi()
# print('Version', __version__)

# 另外用法
from mymodule import *  # 将导入诸如say_hi等所有公共名称，但不会导入__version__名称，因为后者以双下划綫开头
say_hi()

# 警告：要记住避免使用import这种形式，即'from mymodule import'
