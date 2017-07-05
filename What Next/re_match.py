import re

fhand = open("C:/Users/xly/Desktop\poem.txt")
text = fhand.read()

# m = re.search(['use'], text)
# print(re.search(['use'], text))
# print(m)
# print(m.group())

title = 'output_1981.10.21.txt'
y = re.search('\d{4}', title)
m = re.search('\d{2}', title)
d = re.search('\d{2}.txt$', title)

YY = y.group()
MM = m.group()
DD = re.search('\d{2}', d.group()).group()

m = re.search('output_(\d{4}).(\d{2).(\d{2)', title)
print(m.group(1))
print('Today is ', MM, ',', DD, ',', YY)


