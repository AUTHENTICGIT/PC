shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# Indexing or 'Subscription' operation #
# 索引或“下标（Subscription）”操作符 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 从某一字符串中切片
print('character 1 to 3 is', name[1:3])
print('character 2 to end is', name[2:])
print('character 1 to -1 is', name[1:-1])
print('character start to end is', name[:])

# 案例，同上
# 同样可以在切片操作中提供第三个参数，这一参数将被视为切片的步长（Step）（在默认情况下，步长大小为1）
print(shoplist[::1])
print(shoplist[::2])    # 当步长为2时，得到的是第0、2、4 ……位项目
print(shoplist[::3])    # 当步长为3时，得到的是第0、3 ……位项目
print(shoplist[::-1])
