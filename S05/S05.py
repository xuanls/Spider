# 网页图片的爬取以及本地保存

# 图片资源不能直接在爬取的网页内容中获取，需要再次解析并保存二进制文件

import requests
from lxml import etree
import re

url = 'http://spiderbuf.cn/s05/'
myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
html = requests.get(url, headers=myheaders).text
# print(html)
f = open('S05.html', 'w', encoding='utf-8')
f.write(html)
f.close()

# 获取图片资源相对地址
root = etree.HTML(html)
# <img src="/static/images/beginner/1kwfkui2.jpg" class="img-responsive img-thumbnail" alt="python爬取图片">
imgs = root.xpath('//img/@src')
# print(imgs)

# 浏览器查看源码，访问图片的绝对地址 http://spiderbuf.cn/static/images/beginner/1kwfkui2.jpg
# 循环构造请求，保存图片二进制数据到本地
for item in imgs:
    image_data = requests.get( 'http://spiderbuf.cn' + item, headers=myheaders).content
    img = open(str(item).replace('/', '_'), 'wb')   # 替换‘/’，命名合法
    img.write(image_data)
    img.close()