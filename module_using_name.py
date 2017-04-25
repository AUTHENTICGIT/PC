# 当模块第一次被导入时，它所包含的的代码将被执行
# 可以通过这一特性来使模块以不同的方式执行，取决于它是为自己所用还是其他从的模块中导入而来
# 可以通过使用模块的__name__属性来实现

# 案例
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

# 每一个Python模块都定义了它的__name__属性
# 如果它与__main__相同则代表这一模块是由用户独立运行的
