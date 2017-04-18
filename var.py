i = 5
print(i)
i = i + 1
print(i)
print('''This is a multi-line string.
This is the second line.''')
print('This is a multi-line string.\
This is the 2nd line')
print('This is a multi-line string.\nThis is the 2nd line')

a = 9
b = 5
c = a & b   #按位与
print(a, b, c)
a = 9
a = a^15    #按位异或
print(a)
b = 61610
b = b & 255 #高八位清0，保留低8位
print(b)
