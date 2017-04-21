def func(a, b, *c, **d):
    print(a)
    print(b)
    for x in c:
        print(x)
    for k,v in d.items():
        print(k, v)
func('a', 10, 'single_item 1', 'single_item 2', 'single_item 3', Inge=1560, John=2231, Jack=1123)

#案例
def total(a=5, *numbers, **phonebook):
    print('a', a)
    #遍历元祖中的所有项目
    for single_item in numbers:
        print('single_item', single_item)
    for first_part,  second_part in phonebook.items():
        print(first_part, second_part)

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
