# 带验证码的登录爬取

# 手动登陆一次，获取访问的网以及对应的cookie，构造进请求头中，即可绕过登陆（有时效性）

import requests
from lxml import etree

url = 'http://spiderbuf.cn/e02/list'   # 请求url在浏览器中检查得到

payload = {'username': 'admin', 'password': '123456'}
myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                            Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
             'Cookie': 'admin=13a3f548bb1695cd752c41853699c06f'}    # 时效性，更新缓存会消失，重新获取
html = requests.post(url, headers=myheaders, data=payload).text   # 获取网页源码
# print(html)

f = open('e02.html', 'w', encoding='utf-8')
f.write(html)                   # 保存到本地
f.close()

root = etree.HTML(html)
trs = root.xpath('//tr')

f = open('e02.txt', 'w', encoding='utf-8')
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        s = s + str(td.text) + '|'
    if s != '':
        f.write(s + '\n')
f.close()