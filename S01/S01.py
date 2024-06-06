# requests lxml库入门

import requests
from lxml import etree

url = 'http://spiderbuf.cn/s01/'

html = requests.get(url).text   # 获取网页源码
# print(html)

f = open('S01.html', 'w', encoding='utf-8')
f.write(html)                   # 保存到本地
f.close()

root = etree.HTML(html)
trs = root.xpath('//tr')

f = open('S01.txt', 'w', encoding='utf-8')
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        s = s + str(td.text) + '|'
    if s != '':
        f.write(s + '\n')
f.close()



