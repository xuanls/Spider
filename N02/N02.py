# 使用base63编码的图片的爬取与解码还原

import requests
from lxml import etree
import base64

url = 'http://spiderbuf.cn/n02/'
myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
html = requests.get(url, headers=myheaders).text
# print(html)

f = open('N02.html', 'w', encoding='utf-8')
f.write(html)
f.close()

# 获取图片资源相对地址
# src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgA
root = etree.HTML(html)
imgs = root.xpath('//img/@src')
# print(imgs)

for item in imgs:
    item = item.replace('data:image/png;base64,', '')
    str_bytes = item.encode('raw_unicode_escape')
    decoded = base64.b64decode(str_bytes)   # str 转 bytes

    img = open('N02.png', 'wb')
    img.write(decoded)
    img.close()