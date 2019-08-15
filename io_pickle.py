# import pickle
#
# shoplistfile = 'shoplist.data'
# # print(type(shoplistfile), shoplistfile)
# shoplist = ['apple', 'mango', 'carrot']
#
# f = open(shoplistfile, 'wb')
# pickle.dump(shoplist, f)
# print(type(shoplistfile), shoplistfile)
# f.close()
#
# del shoplist
#
# f = open(shoplistfile, 'rb')
# comment = pickle.load(f)
# print(comment)

# 案例
import pickle
# 我们存储相关对象的文件的名称
shoplistfile = 'shoplist.data'
# 需要购买的物品清单
shoplist = ['apple', 'mango', 'carrot']

# 准备写入文件
f = open(shoplistfile, 'wb')
# 转储对象至文件
pickle.dump(shoplist, f)
f.close()

# 清除 shoplist 变量
del shoplist

# 重新打开存储文件
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)