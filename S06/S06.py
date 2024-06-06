# 带iframe的页面源码分析及数据爬取

# <iframe src="/inner" width="100%" height="800" scrolling="no" marginheight="0" marginwidth="0" border="0" frameborder="no"></iframe>
# 请求的网页中并没有数据，而是用iframe嵌套另一个网页，浏览器调试找出进行替换即可

import requests
from lxml import etree

# url = 'http://spiderbuf.cn/s06/'      # 只有框架
url = 'http://spiderbuf.cn/inner/'      # 真正存放数据的地方

myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
html = requests.get(url, headers=myheaders).text
# print(html)
f = open('S06.html', 'w', encoding='utf-8')
f.write(html)
f.close()

root = etree.HTML(html)
trs = root.xpath('//tr')

f = open('S06.txt', 'w', encoding='utf-8')
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        s = s + str(td.xpath('string(.)')) + '|'  # xpath进一步解析，过滤标签
    print(s.replace('\n', '').replace(' ', ''))
    if s != '':
        f.write(s.replace('\n', '' )  + '\n')
f.close()