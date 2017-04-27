zoo = 'python', 'elephant', 'penguin'
print('Number of animals in the zoo is', len(zoo))

newzoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(newzoo))
print('All animals in new zoo are', newzoo)

print('Animals brought from old zoo are', newzoo[2])
print('Last animals brought from old zoo is', newzoo[2][2])
print('Number of animals in the new zoo is', len(newzoo)-1 + len(zoo))

# 案例
# 我会推荐你总是使用括号
# 来指明元祖的开始与结束
# 尽管括号是一个可选选项
# 明了胜过晦涩，显式优于隐式
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animals brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo)-1 + len(newzoo[2]))
