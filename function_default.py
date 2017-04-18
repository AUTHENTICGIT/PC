def say(s, count = 1):  # 只有参数列表末尾的参数才能被赋予默认参数值
    print(s * count)

say('Hello')
say('World', 5)

# 案例
def say(message, times=1):
    print(message * times)

say('Hello')
say('World', 5)
