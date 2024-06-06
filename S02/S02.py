# http请求分析及头构造使用

import requests
from lxml import etree

url = 'http://spiderbuf.cn/s02/'
# 直接get会显示403 Forbidden

myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
html = requests.get(url, headers=myheaders).text   # 获取网页源码
# print(html)

f = open('S02.html', 'w', encoding='utf-8')
f.write(html)                   # 保存到本地
f.close()

root = etree.HTML(html)
trs = root.xpath('//tr')

f = open('S02.txt', 'w', encoding='utf-8')
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        s = s + str(td.text) + '|'
    if s != '':
        f.write(s + '\n')
f.close()



