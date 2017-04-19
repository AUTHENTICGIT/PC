# 函数
def say_hello():
    print('Hello world')
say_hello()
say_hello()
# 函数参数
def maxium(a, b):
    if a < b:
        print(b)
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(a)
maxium(1, 3)
maxium(3, 3)
maxium(1, 5)
#局部变量
def func(x):
    print(x)
    x = 1111
    print('x is changes to', x)
x = 5
func(x)
print('real x is', x)
#全局变量
def func1():
    global x
    x *= 0
    print(x)
x = 5
func1()
#默认参数值
def func2(x, y=18):
    print('name:',x, '\t' 'age:', y)
func2('Apple')
func2('Bella', 21)
func2('Cindy', 16)
#关键字参数
def func3(a, b=5, c=10):
    print('a is', a, 'b is', b, 'c is', c)
func3(2, 1, c=3)
func3(2, 1)
func3(c=11, a=7)
#可变参数
def func(a, b, *c, **d):
