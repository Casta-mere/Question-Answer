from xml.dom.minidom import Element
import requests
import time
import json
import threading
from bs4 import BeautifulSoup as Bs
from urllib import parse
from urllib.error import URLError  # 异常处理模块，捕获错误
from urllib.request import ProxyHandler, build_opener  # 代理IP模块

ans_dir = "data/ans/info_Google.json"


# 获取代理ip
def get_proxy():
    score = 1
    while score < 98:
        ip, score = requests.get(
            "http://10.11.195.12:1111/fetch").json()["proxy"]
    return {"http": f'http://{ip}'}


global p
p = get_proxy()


class myThread (threading.Thread):
    def __init__(self, item_name, item_id):
        threading.Thread.__init__(self)
        self.item_name = item_name
        self.item_id = item_id

    def run(self):
        item_name = self.item_name
        global p
        ans = []

        # 下拉框

        # get from Google
        proxy_handler = ProxyHandler({
            'https': '127.0.0.1:7890'

        })
        opener = build_opener(proxy_handler)
        Google_headers = (
            'user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        )
        opener.addheaders = [Google_headers]

        try:
            url = f"https://www.google.com/complete/search?q={parse.quote(item_name)}&cp=2&client=gws-wiz&xssi=t&hl=zh-CN"
            Google_response = opener.open(url)  # 此处的open方法同urllib的urlopen方法
            Google_ans = Google_response.read().decode('utf-8').split("\n")[1]

            content = json.loads(Google_ans)
            for i in range(len(content[0])):
                if(content[0][i][0] not in ans):
                    ans.append(content[0][i][0])

        except URLError as e:
            print(e.reason)

        # 下拉框写入
        if len(ans) > 0:
            flag = True
            content = f'\t\t"{item_name}":[\n'
            for i in ans:
                if(flag):
                    flag = False
                    content += ('\t\t\t["'+i+'",0]')
                # if(Question(i))
                else:
                    content += (',\n\t\t\t["'+i+'",0]')
        else :
            return
        # 相关搜索
        ans = []

        

        content += ("\n\t\t],\n")
        # writeback
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        with open(ans_dir, "a", encoding="utf-8") as f:
            f.write(content)
        # print("Ending " + self.string)
        threadLock.release()


# 使用多线程获取联想问题
threadLock = threading.Lock()
global threads
threads = []


def get_info(stringarray, id):
    global threads
    for string in stringarray:
        thread = myThread(string, id)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    threads = []


back = ['', ' ', '是', '什么时候', '怎么', '在', '的', '得', '地', '什么', '哪',
            '有', '在哪', ' 英文', '品种', '价格', '作用', '时间', '地点', '为什么', '可以']

if __name__ == "__main__":
    T1 = time.perf_counter()
    t = T1
    flag = True
    with open("info_dict.json", encoding="utf-8") as json_file:
        attrbute = json.load(json_file)
        print("load json file success")
        T1 = time.perf_counter()
        t=T1
        with open("data.txt", encoding="utf-8") as data_f:
            line = data_f.readline()
            count = 0
            while line:  # 每行一个实体
                if(count == 500):
                    break
                count += 1
                item_name = line.split(",")[0]
                item_id = line.split(",")[1].split("\n")[0]
                try:
                    attr = attrbute[item_id]['basicInfo']
                except:
                    element=1
                
                string = []

                for i in back:
                    string.append(item_name+i)
                for i in attr:
                    if(i not in back):
                        string.append(item_name+i)

                if(flag):
                    flag = False
                    with open(ans_dir, "a", encoding="utf-8") as f:
                        f.write('{\n\t"'+item_id+"_"+item_name+'": {\n')
                    get_info(string, item_id)
                    with open(ans_dir, "a", encoding="utf-8") as f:
                        f.write('\t\t"": ""\n\t}')
                else:
                    with open(ans_dir, "a", encoding="utf-8") as f:
                        f.write(',\n\t"'+item_id+"_"+item_name+'": {\n')
                    get_info(string, item_id)
                    with open(ans_dir, "a", encoding="utf-8") as f:
                        f.write('\t\t"": ""\n\t}')
                print(f"{item_name} done, cost time: {time.perf_counter()-T1}")
                T1 = time.perf_counter()
                line = data_f.readline()
            data_f.close()
            with open(ans_dir, "a", encoding="utf-8") as f:
                f.write("\n}")

    print(time.perf_counter()-t)
