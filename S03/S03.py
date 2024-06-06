# lxml进阶语法与解析练习
# 增加了表格干扰

import requests
from lxml import etree

url = 'http://spiderbuf.cn/s03/'
# 直接get会显示403 Forbidden

myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
html = requests.get(url, headers=myheaders).text   # 获取网页源码
# print(html)

f = open('S03.html', 'w', encoding='utf-8')
f.write(html)                   # 保存到本地
f.close()

# 可以正常请求网页并保存，但解析出错
root = etree.HTML(html)
trs = root.xpath('//tr')

f = open('S03.txt', 'w', encoding='utf-8')
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        s = s + str(td.xpath('string(.)')) + '|'    # xpath进一步解析，过滤标签
        # s = s + str(td.text) + '|'
        #         <tr>
        #             <td>1</td>
        #             <td><a href="#">172.16.80.178</a></td>
        #             <td>CD-82-76-71-65-75</td>
        #             <td>堡垒机</td>
        #             <td>服务器</td>
        #             <td>Windows10</td>
        #             <td>80,22,443</td>
        #             <td><font color="green">在线</font></td>
        #         </tr>
        # 因为有标签元素，所以会显示None
        # |None|CD-82-76-71-65-75|堡垒机|服务器|Windows10|80,22,443|None|
    if s != '':
        f.write(s + '\n')
f.close()



