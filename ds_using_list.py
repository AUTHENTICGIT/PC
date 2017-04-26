purchar = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(purchar), 'items to purchase.')

print('These items are:')
for i in purchar:
    print(i, end=' ')

print('\nI also have to buy')
purchar.append('rice')
print('My shopping list is now', purchar)

print('I will sort my list now')
purchar = sorted(purchar)
print('Sorted shopping list is', purchar)

print('The first item I will buy is', purchar[0])
print('My shopping list is now', purchar[1:])

# 案例
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase')

print('These items are:')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now.')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
