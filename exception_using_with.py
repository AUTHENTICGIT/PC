# with open('C:/Users/xly/Desktop\poem.txt') as fhand:
#     for line in fhand:
#         print(line)

# 案例
with open("C:/Users/xly/Desktop\poem.txt") as f:
    for line in f:
        print(line, end='')

# fhand = open("C:/Users/xly/Desktop\poem.txt")
# fhand.close()
# for line in fhand:
#     print(line)

class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"
    def __exit__(self, type, value, trace):
        print('In __exit__()')
def get_sample():
    return Sample()
with get_sample() as sample:
    print("sample:", sample)
