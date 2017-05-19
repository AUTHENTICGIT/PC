# with open('C:/Users/xly/Desktop\poem.txt') as fhand:
#     for line in fhand:
#         print(line)

# 案例
with open("C:/Users/xly/Desktop\poem.txt") as f:
    for line in f:
        print(line, end='')

fhand = open("C:/Users/xly/Desktop\poem.txt")
fhand.close()
for line in fhand:
    print(line)
