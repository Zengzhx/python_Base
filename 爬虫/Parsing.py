from urllib.parse import *


o = urlparse('https://www.baidu.com?aaa=nanem') #解析地址
print(o)

j = urljoin('https://www.baidu.com?aaa=nanem','aaa.html')
print(j)


