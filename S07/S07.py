# ajax动态加载数据的爬取

# js动态渲染，从源代码中获取真正的数据地址
# <script  type="text/javascript">
#   $('#mytable').bootstrapTable({
#       url: '/iplist',

import requests
import json     # 解析json文件

# url = 'http://spiderbuf.cn/s07/'    # 框架
url = 'http://spiderbuf.cn/iplist'
myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
data_json = requests.get(url, headers=myheaders).content    # 保存为text中文会乱码
# print(data_json)

f = open('S07.json', 'wb')
f.write(data_json)
f.close()

# 解码为python对象
ls = json.loads(data_json)
# print(ls)

f = open('S07.txt', 'w', encoding='utf-8')
for item in ls:
    s = '%s|%s|%s|%s|%s|%s|%s|' % (item['ip'], item['mac'], item['name'], item['type'],
                                   item['manufacturer'], item['ports'], item['status'])
    f.write(s + "\n")
f.close()