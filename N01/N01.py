# User-Agent与Referer校验反爬

# Referer字段告诉了服务器，用户在访问当前资源之前的位置,用来用户跟踪

import requests
from lxml import etree
import re

base_url = 'http://spiderbuf.cn/n01'     # 构造url列表
myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                            Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
             'Referer': 'http://spiderbuf.cn/list?pageno=2'}
html = requests.get(base_url, headers=myheaders).text  # 获取网页源码
# print(html)

f = open('N01.html', 'w', encoding='utf-8')
f.write(html)
f.close()
# 定位元素
# < div class ="container" >
# < div class ="row" style="margin-top: 30px" >
# < div class ="col-xs-6 col-lg-4" style="margin-bottom: 30px;" >
# < h2 > 腾讯控股 < / h2 >
# < p > 排名：1 < / p >
# < p > 企业估值(亿元)：39000 < / p >
# < p > CEO：马化腾 < / p >
# < p > 行业：互联网服务 < / p >
# < / div > <!-- /.col - xs - 6. col - lg - 4 -->
root = etree.HTML(html)
ls=root.xpath('//div[@class="container"]/div/div')    # 获取文本数据
# page_text = ls[0].xpath('string(.)')
# print(page_text)

f = open('N01.text', 'w', encoding='utf-8')
for item in ls:
    hnodes = item.xpath('./h2')
    pnodes = item.xpath('./p')

    s0 = hnodes[0].text
    s1 = pnodes[0].text
    s2 = pnodes[1].text
    s3 = pnodes[2].text
    s4 = pnodes[3].text
    # 腾讯控股排名：1企业估值(亿元)：39000CEO：马化腾行业：互联网服务
    s = (s0 + '|' + s1.replace('排名：', '') + '|' + s2.replace('企业估值(亿元)：', '') + '|'
         + s3.replace('CEO：', '') + '|' + s4.replace('行业：', '') + '\n')
    f.write(s)
f.close()
    



















