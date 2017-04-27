address = {'Swaroop':'swaroop@swaroopch.com', 'Matsumoto':'matz@ruvy-lang.org', 'Larry':'larry@wall.org'}

print('Swaroop\'s address is', address['Swaroop'])

print('\nThere are', len(address), 'contacts in the address-book\n')

for k,v in address.items():
    print('Contact', k, 'at', v)

address['Guido'] = 'guido@python.org'
print('\nGuido\'s address is', address['Guido'])

# 案例
# "ab"是地址（Address）簿（Book）的缩写

ab = {
    'Swaroop': 'swaroop@swaroop.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruvy-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一对键值-值配对
del ab['Spammer']

print('\nThere are {} contacts in the address book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# 添加一对键值-值配对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
