# 无序号翻页爬取

# 通过解析网页爬取相应页面的标签，构造url列表

import requests
from lxml import etree

base_url = 'http://spiderbuf.cn/e03'     # 构造url列表
myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                            Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
html = requests.get(base_url, headers=myheaders).text  # 获取网页源码
# print(html)

# 取页数
# <ul class="pagination">
#     <li><span>共5页</span></li>
#     <li><a href="./2fe6286a4e5f">1</a></li>
#     <li><a href="./5f685274073b">2</a></li>
#     <li><a href="./279fcd874c72">3</a></li>
#     <li><a href="./8a3d4d640516">4</a></li>
#     <li><a href="./fbd076c39d28">5</a></li>
# </ul>
root = etree.HTML(html)
lis = root.xpath('//ul[@class="pagination"]/li/a/@href')    # 获取页面的url值
# print(lis)
i = 1
for item in lis:
    url = base_url + item.replace('.', '')
    html = requests.get(url, headers=myheaders).text
    f = open('E03_%d.html' % i, 'w', encoding='utf-8')
    f.write(html)                   # 保存到本地
    f.close()

    root = etree.HTML(html)
    trs = root.xpath('//tr')

    f = open('E03_%d.txt' % i, 'w', encoding='utf-8')
    for tr in trs:
        tds = tr.xpath('./td')
        s = ''
        for td in tds:
            s = s + str(td.xpath('string(.)')) + '|'    # xpath进一步解析，过滤标签
        if s != '':
            f.write(s + '\n')
    f.close()
    i += 1

