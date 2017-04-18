x = 5

def change(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

change(x)
print('x is still', x)

# 案例
x = 5

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)
