from genericpath import exists
import requests
import time
import json
import threading
from bs4 import BeautifulSoup as Bs
from urllib import parse
from urllib.error import URLError  # 异常处理模块，捕获错误
from urllib.request import ProxyHandler, build_opener  # 代理IP模块

ans_dir = "data/info_Baidu.json"


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
    def __init__(self,item, item_name):
        threading.Thread.__init__(self)
        self.item_name = item_name
        self.item=item

    def run(self):
        item_name = self.item_name
        global p
        ans = []
        length=self.item.__len__()
        # 下拉框

        # get from Baidu
        Baidu_url = f"https://www.baidu.com/sugrec?pre=1&p=3&ie=utf-8&json=1&prod=pc&from=pc_web&sugsid=36546,36464,36825,36454,36413,36692,36166,36816,36774,36708,36745,36761,36770,36764,26350,36862&wd={parse.quote(item_name)}&req=2&bs={parse.quote(item_name)}&pbs={parse.quote(item_name)}&csor=1&cb=jQuery110207781353213512758_1658460562321&_=1658460562343"
        Baidu_response = requests.get(Baidu_url, proxies=p)
        if(Baidu_response.status_code != 200):
            p = get_proxy()
            Baidu_response = requests.get(Baidu_url, proxies=p)
        try:
            text = Baidu_response.text.split("(")[1].split(")")[0]
            j = json.loads(text)
            for i in j["g"]:
                    ans.append(i["q"].replace(self.item,"{}"))
        except:
            element = 1

        # 下拉框写入
        if len(ans) > 0:
            flag = True
            content = ''
            for i in ans:
                if(flag):
                    flag = False
                    content += ('\t\t"'+i.replace('"',"").replace("'","")+'",\n')
                # if(Question(i))
                else:
                    content += ('\t\t"'+i.replace('"',"").replace("'","")+'",\n')
        else:
            return

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


def get_info(item_name,stringarray):
    global threads
    for string in stringarray:
        thread = myThread(item_name,string)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    threads = []


back = ['', ' ', '是', '什么时候', '怎么', '在', '的', '得', '地', '什么', '哪',
            '有', '在哪', ' 英文', '时间', '地点', '为什么', '可以',
            '别名', '字', '号', '本名', '墓葬地', '去世地', '所处时代', '主要作品','逝世日期','出生日期','主要成就','爵位','官职','后世地位','谥号','民族','籍贯']


def run():
    T1 = time.perf_counter()
    t = T1
    flag = True
    if exists (ans_dir):
        with open(ans_dir, "w", encoding="utf-8") as f:
            f.write('')
    with open("Poets.txt", "r", encoding="utf-8") as f_1:
        line = f_1.readline()
        for i in range(0, 6000):
            item_name = line.split("\n")[0]
            string = []
            for i in back:
                string.append(item_name+i)

            if(flag):
                flag = False
                with open(ans_dir, "a", encoding="utf-8") as f:
                    f.write('{\n\t"'+item_name+'": [\n')
                get_info(item_name,string)
                with open(ans_dir, "a", encoding="utf-8") as f:
                    f.write('\t\t""\n\t]')
            else:
                with open(ans_dir, "a", encoding="utf-8") as f:
                    f.write(',\n\t"'+item_name+'": [\n')
                get_info(item_name,string)
                with open(ans_dir, "a", encoding="utf-8") as f:
                    f.write('\t\t""\n\t]')
            print(f"{item_name} done, cost time: {time.perf_counter()-T1}")
            T1 = time.perf_counter()
            line = f_1.readline()

        with open(ans_dir, "a", encoding="utf-8") as f:
            f.write("\n}")

    print(time.perf_counter()-t)


if __name__ == "__main__":
    run()
