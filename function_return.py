def maximum(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return 'They are equal'
print(maximum(2, 3))

# 案例
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2, 3))

# 每一个函数都在其末尾隐含了一句return None
def some_function():
    pass    # Python中的pass语句用于指示一个没有内容的语句块

# 有内置函数max实现了“找到最大数”的功能
print(max(2, 3))
