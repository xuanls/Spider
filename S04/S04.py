# 分页参数分析及翻页爬取

# ① 写死页数，循环访问
# ② xpath解析，正则获取页数
# ③ pagesize获取更多数据，减少访问次数（）

import requests
from lxml import etree
import re   # 正则表达式

base_url = 'http://spiderbuf.cn/s04/?pageno=%d'     # 构造url列表
# base_url = 'http://spiderbuf.cn/s04/?pageno=1&pagesize=50'  # 一次性获取所有数据，下面正常访问爬取
myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
# print(html)

# 取页数
html = requests.get(base_url % 1, headers=myheaders).text  # 获取网页源码
root = etree.HTML(html)
# <ul class="pagination">
#    <li><span>共5页</span></li>
lis = root.xpath('//ul[@class="pagination"]/li')
page_text = lis[0].xpath('string(.)')
max_no = re.findall('[0-9]' , page_text)

for i in range(1, int(max_no[0]) + 1):
    url = base_url % i
    html = requests.get(url, headers=myheaders).text
    f = open('S04_%d.html' % i, 'w', encoding='utf-8')
    f.write(html)                   # 保存到本地
    f.close()

    root = etree.HTML(html)
    trs = root.xpath('//tr')

    f = open('S04.txt_%d' % i, 'w', encoding='utf-8')
    for tr in trs:
        tds = tr.xpath('./td')
        s = ''
        for td in tds:
            s = s + str(td.xpath('string(.)')) + '|'    # xpath进一步解析，过滤标签
        if s != '':
            f.write(s + '\n')
    f.close()



