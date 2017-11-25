import urllib.parse

# req = urllib.request.Request(url='http://localhost/cgi-bin/aaa.py')
#
# with urllib.request.urlopen(req) as f:
#     print(f.read().decode('utf-8'))
#

data = {}
data['word'] ='jecvay&Notes'
print(data)

url_value = urllib.parse.urlencode(data)#参数转换
url = 'http://www.baidu.com/?'
full_url = url+url_value
print(full_url)

