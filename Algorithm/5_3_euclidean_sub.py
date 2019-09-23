a = 42
b = 12

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print("最大公约数", a)
