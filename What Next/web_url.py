import urllib.request

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
print(fhand.read())
print(fhand.status)
print(fhand.getheaders())
print(fhand.getheader('Server'))

response = urllib.request.urlopen('http://www.python.org')
print(response.read())
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
