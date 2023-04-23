import requests
import time
import json
import threading
from urllib import request, response
from baiduspider import BaiduSpider
from pprint import pprint
from bs4 import BeautifulSoup as Bs
from urllib import parse

def get_proxy():
    score = 1
    while score < 98:
        ip, score = requests.get(
            "http://10.11.195.12:1111/fetch").json()["proxy"]
    return {"http": f'http://{ip}'}

proxies = {
    'https': 'https://127.0.0.1:7890',
    'http': 'http://127.0.0.1:7890'
}
# url = r'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&'
kw="李白"
print(get_proxy())
# param={
#     'wd':kw
# }
# head={
#     'Host':'www.baidu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
# }
# re=requests.get(url,params=param,headers=head,proxies=get_proxy())
# soup=Bs(re.text,'html.parser')
# list=soup.find_all('a',class_='rs-link_2DE3Q c-line-clamp1 c-color-link')
# for i in list:
#     print(i.text.split("\n")[1].split("                        ")[1])
# with open("test.html","w",encoding="utf-8") as data:
#     data.write(re.text)

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
# url=f"https://www.google.com/complete/search?q={parse.quote(kw)}&cp=2&client=gws-wiz&xssi=t&hl=zh-CN"
# print(url)
# responsn=requests.get(url,proxies=proxies,headers=headers)
# print(responsn.text)


# url="https://cn.bing.com/search?q=%E6%9D%8E%E7%99%BD&qs=n&form=QBRE&sp=-1&pq=%E6%9D%8E%E7%99%BD&sc=7-2&sk=&cvid=464FB8ED811A48A298709BA8463B0A5C&ghsh=0&ghacc=0&ghpl=&count=50"
# url="https://cn.bing.com/search?q=%e6%9d%8e%e7%99%bd&qs=n&sp=-1&pq=%e6%9d%8e%e7%99%bd&sc=7-2&sk=&cvid=48224D992EEF4F4AAFF3289D9AA3B795&ghsh=0&ghacc=0&ghpl=&first=21&FORM=PERE1"
# https://www.bing.com/search?q=%E6%9D%8E%E7%99%BD&form=ANNTH1&count=1

url="https://www.bing.com/search?q=%E6%9D%8E%E7%99%BD&form=ANNTH1&count=1"
response=requests.get(url)
print(response.text)