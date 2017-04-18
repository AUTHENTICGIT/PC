# def func(a, b=5, c=10):
#     print('a is', a, 'b is', b, 'c is', c)
#
# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)
#
# # 案例，同上
def one(**x):
    # 将传入的关键字参数的值保存为元祖输出
    print(x)
    b = ()
    for a in x.values():
        b = b + (a,)
    print(b)
dect = {'one':1, 'two':2, 'three':3}
one(**dect)
