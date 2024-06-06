# CSS样式偏移混淆文本内容的解析与爬取

import requests
from lxml import etree
import re

base_url = 'http://spiderbuf.cn/h01'  # 构造url列表
myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                            Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
             'Referer': 'http://spiderbuf.cn/list?pageno=2'}
html = requests.get(base_url, headers=myheaders).text  # 获取网页源码
# print(html)

f = open('H01.html', 'w', encoding='utf-8')
f.write(html)
f.close()

# 定位元素
# < div class ="container" >
# < div class ="row" style="margin-top: 30px;width: 800px;" >
# < / div >
# < div class ="row" style="margin-top: 30px" >
# < div class ="col-xs-6 col-lg-4" style="margin-bottom: 30px;" >
# < h2 > < i
# style = "width: 32px;position: relative; left: 32px;" > 讯 < / i > < i
# style = "width: 32px;position: relative; left: -32px;" > 腾 < / i > < i
# style = "width: 32px;position: relative;" > 控 < / i > < i
# style = "width: 32px;position: relative;" > 股 < / i > < / h2 >
# < p > 排名：1 < / p >
# < p > 企业估值(亿元)： < i
# style = "width: 14px;position: relative; left: 10px;" > 9 < / i > < i
# style = "width: 14px;position: relative; left: -10px;" > 3 < / i > < i
# style = "width: 14px;position: relative;" > 0 < / i > < i
# style = "width: 14px;position: relative;" > 0 < / i > < / p >
# < p > CEO：马化腾 < / p >
# < p > 行业：互联网服务 < / p >
# < / div > <!-- /.col - xs - 6. col - lg - 4 -->
root = etree.HTML(html)
ls = root.xpath('//div[@class="container"]/div/div')  # 获取文本数据
# page_text = ls[0].xpath('string(.)')
# print(page_text)

f = open('H01.text', 'w', encoding='utf-8')
for item in ls:
    hnodes = item.xpath('./h2')
    pnodes = item.xpath('./p')

    # 由于CSS样式，部分内容反转，手动修改样式
    # <i left: 32px;">讯</i><i left: -32px;">腾</i>
    # 讯腾控股 | 1 | 9300 | 马化腾 | 互联网服务
    temp = hnodes[0].xpath('string(.)')
    s0 = temp[1: 2] + temp[0: 1] + temp[2:]
    s1 = pnodes[0].text
    temp = pnodes[1].xpath('string(.)').replace('企业估值(亿元)：', '')
    s2 = temp[1: 2] + temp[0: 1] + temp[2:]
    s3 = pnodes[2].text
    s4 = pnodes[3].text

    s = (s0 + '|' + s1.replace('排名：', '') + '|' + s2 + '|'
         + s3.replace('CEO：', '') + '|' + s4.replace('行业：', '') + '\n')
    f.write(s)
f.close()




















