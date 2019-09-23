a = 42
b = 12

mod = a%b
while mod != 0:
    y = mod
    mod = b%mod
print("最大公约数",y)
