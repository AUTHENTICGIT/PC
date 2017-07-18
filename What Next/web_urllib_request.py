import urllib.request
import urllib.parse

data1 = urllib.parse.urlencode({'word': 'hello'}).encode(encoding = 'utf-8')
data2 = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
print(data1)
print(data2)
# request = urllib.request.urlopen('http://httpbin.org/post', data = data)
