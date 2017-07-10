import urllib.request
import re

# 全部PNG
request = urllib.request.urlopen('http://www.baidu.com')
resource = request.read().decode()  # read获取的类型为bytes，用encode()解码成str
print(re.findall('http://.+\.png' ,resource))

