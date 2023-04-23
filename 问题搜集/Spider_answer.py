import requests
import time
import json
import threading
from bs4 import BeautifulSoup as Bs
from urllib import parse
from urllib.error import URLError  # 异常处理模块，捕获错误
from urllib.request import ProxyHandler, build_opener  # 代理IP模块

ans_dir = "data/ans/ans.json"
json_dir = "data/info_all.json"

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
    def __init__(self, question, item_name):
        threading.Thread.__init__(self)
        self.question = question
        self.item_name = item_name

    def run(self):
        question = self.question.split("_")[1]
        global p

        # get from Bing
        headers = {
            "cookies": "SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=41E060320BE94F829AC2DD21A3D21AF0&dmnchg=1; MUID=02B792634CBA6A751C1D9D7C4DC56B7F; _ITAB=STAB=TR; MUIDV=NU=1; _TTSS_IN=hist=WyJ6aC1IYW5zIiwiZW4iLCJhdXRvLWRldGVjdCJd; MUIDB=02B792634CBA6A751C1D9D7C4DC56B7F; SnrOvr=X=rebateson; _RwBf=W=1&r=1&mta=0&rc=126&rb=126&gb=0&rg=0&pc=126&mtu=0&rbb=0.0&g=0&cid=&v=2&l=2021-11-23T08:00:00.0000000Z&lft=00010101&aof=0&o=0&p=MSRLAUNCHERAPP201805&c=MR000I&t=4945&s=2021-03-20T23:27:43.6748591+00:00&ts=2021-11-24T07:20:12.9037975+00:00&rwred=0&e=2RJbUeT8NCYtKCfJJYgHOHFw0i1UIP8XDsAQ49Kztj_4ybrnkTyGuoPHwA-1R-65nVzgcDAFavWWwGhoJWBRdg&A=220A99376FB293C916B649F8FFFFFFFF; _tarLang=default=zh-Hans; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnQiLCJ6aC1IYW5zIl0=; _EDGE_CD=u=zh-hans&m=zh-cn; _UR=MC=1&QS=3&TC=C0&TQS=3; _clck=fsoq58|1|f1q|0; imgv=lodlg=5&gts=20210826&flts=20220616; ANON=A=220A99376FB293C916B649F8FFFFFFFF&E=1b25&W=1; _HPVN=CS=eyJQbiI6eyJDbiI6MCwiU3QiOjIsIlFzIjoxLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MCwiU3QiOjEsIlFzIjoxLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MzcsIlN0IjoxLCJRcyI6MCwiUHJvZCI6IlQifSwiQXAiOnRydWUsIk11dGUiOnRydWUsIkxhZCI6IjIwMjItMDctMjFUMDA6MDA6MDBaIiwiSW90ZCI6MCwiR3diIjowLCJEZnQiOm51bGwsIk12cyI6MCwiRmx0IjowLCJJbXAiOjQyfQ==; BFB=AhBwoSdXKbnRXi768ticlR8tliyXnuF_SzEs1jYXh5LkkJjOjZAh_iZ4p6LRrb_5G9Zn5z-uk54dzmOfrcSIVpEzHu2vpbt-VSbQGR33aacaAxgQ3hmmocDVbs7Gzv447dpDNq3LLnGs50URgBH19oh1EOWy8Ft-dzCw0zYHSs9huA; OIDR=ghAJ3yG9eulJLCpxBDPgNWe9YGv1iFUmkfrHfjo2Rm4dI8s-CujV6tnVA4si1VO6ag5LDRqDzcsiujMBiF7v59nBNQ6QvuN4Gh_IfqX-mldpUVHX5t543fDvJDmwXK0djKc6ew2IdG7zdWAVuGVBe7jfmnS-4QYxnLZuljLKCiGUa0gl_Y9aTJF3HTFCxHOcoqLVqQvF4AW5d7fIASXxosQzSQgZuGjnIqD2-iyuUx1PRHLWvi-W7LXGNzhHUlRsk75099aTnfV-kfMn5cuPpp1tOQuFjs08yUnTdmMCyy1kOj2qToHTwpjCC8l4cpxoo-IidCOImc0s0Ijtj7YAv4hDch178LMKKzLQ0AP5tDCNOw9KdCfioMvsduCLYuhFfrYwBsPco65fkLkZ0HqM5HIyKiPLYT9pHOLqyAfxQfPut4jHM13CCbKrFobKcOlqrDy6tN6qw3xxUwdnypaU1wi_U6qlXDvXteMd0SU6R0wNS1TenrM8SIu5IFGzTadWeiwLdXb4Hdbq92CYiETZVwE0EOtugtNRGOXtQP6tB4Z4Dm3aNCHxlSb-actnve7PR2yw_zmy-pD0ov7YloTxjfI-B2ebsTC-w3k9vjYNoWF3xdmQTdO91hL-RTcBoGgrSBsnTQ9euc-IHDyVU0lN8iW2y-5nPIn7TYFxLg0890kjCnAFeMRQaapVkVA2Cd12B3D3GwEQGYBJ7lXjc9JuQQ7yvwaAwE8055sQgWfAPBDx45ShpgzvLeUMpB9peyb9eldmDA5h70qBKMU9ievXGsb4hBABYeSaia_-3DBVEvplmmhcJ7k_bQ8R3h7dmNJOVFNo1RqKsfjvrGMY_HBpMVQoPEEQXY3BkTK5BhDjYTaopTfqApzQMuoRrEwjFADarMtY2rwrw5hXel35C3V3ZE4tUD00qvZ9xFxarAUtoUaY35IpOUu0rbxMPW91ya28QdJ6Cx3E4MB1LmglPo9hXIgxT4v_2_972pMHl3EUEEzys45MX5vnqskrvbAacHaF9iSscTIogKwM7uGc4dKo3FjTtp06z1Bwz2UiAasgs0uJnC1333iuek24_e2wdJr_KVJhzFx6aIVi2NyrfGDRtEkcLo3EcpBVR9hV3g6V6SSINzQEjmsarraT5yzCsgoBiL--dUe_94t4IrZpOask4cze; SRCHUSR=DOB=20200807&T=1632741452000&POEX=W; BFBUSR=BAWAS=1&BAWFS=1; ZHCHATSTRONGATTRACT=TRUE; HOOKBLOCKINDICATOR=TRUE; _EDGE_S=SID=2371C47CE9C4664D031AD588E8C5678A; WLS=C=edac5ceb5db4f577&N=%e6%97%ad%e5%88%9a; _U=1nUE5fvgYmC2Huoyl8ZPvZ3nksV02l6Uj3pW5kaS1ZQelWSKxYdXzE3NpQ1QYb_RcWBQw3_6fbi23xMlvkUZzgLHwgFeeIZOBlCmMSMUqegqGvL-RSdIGEUrjpfyO7MIaW45N0dJwBwt9CFHmCAB67SN80u4t8GbeKb6BvYpwcbziap-Y5LxmUqbt0lVFiMbKeGV9TPTpOj92VLOC7SOtKg; _SS=SID=2371C47CE9C4664D031AD588E8C5678A&PC=U531; SRCHS=PC=U531; ipv6=hit=1659407192224&t=4; SUID=A; ZHCHATWEAKATTRACT=TRUE; SNRHOP=I=&TS=; ABDEF=V=13&ABDV=11&MRNB=1659406562286&MRB=0; USRLOC=HS=1&RL=0&DLOC=LAT=30.316326725362035|LON=120.34897445608843|A=83|N=%e6%9d%ad%e5%b7%9e%e5%b8%82%e9%92%b1%e5%a1%98%e5%8c%ba|C=|S=|TS=220802021602|ETS=220802022602|; OID=ghAUP8AL1bVsCGcl3kibP-ltGhqf6z3do6xNsn7UkaoBXxF_2pz_lzdJlSGgJPItyEsHRcvL7AiC_JSo8KHJkhx_UQOfcko2krf3WlPbkM0arioNe-3uhbHMUUALa59I9Dhs5KxvsTzqut1oJxFghmItztwO_Z_-RnZC_eRk2CEUi_6HJu2xN_1glVOlT9VYpkBxM4PkYTnumXaAaQ3WRPJkZj0_A4URqcXRwgSd1rxgh7O78FR-GuQgWag6q3nxQtEkpg3rUM6-Q7FgEUCY7suvaperofSknJSl11uSXHjHT6oVhZT_IB6qBQkc867MCin4CNlqtNe-EImoj3dOkBitiT1J9uFLFjawmRPcpa22UM5aR8SXhoS1hg2hBFVu-84sqhp5QSPXCsWp7dYLX3QcPyB31FWceOWyGI_JxGjzPr0PokjJKcbGlDeXoqlDVBMQgmb-XSVM-YiRehx53xCSWIBv5SuHJyxawSdhKaVs_8biXp9eopWDyWBs5jZn2wo44FwCFKPgP4ioNE6RBuxjL8uU2V0WidJnxeQ8DcESmSlo_HYmBaXuYC145g3k-SmsBsYb66sNoRSvIcnAqvuF3EqLas0Nu1j9H7n4XiRZeiRG-YckOmkzwUqc1Mzmj9YahsNmtu2Qivrsp58gbl0MMe1XcWaWBG21U1j5L2cOtnNZKqGcziNIaJ8TV4nBWSkYpTGsiOJ9J_LEq-h9hXEHezeppRUfiw6QV4m_y0sX_SxsdNvtG7qWCLq2NQt7w5tuUDYO0_WgEFr9Cvd4kGqUoYBJI8WoDo_WPm5DHEv4Ppr4QUQ71Y8cih4C0DJB8j5pflarPvmUcnU-OT0KOnkHIGYVRx1Kc7fOMg5okAGwng4_txOIwUyYBCXXZYZU3wrvAmfm6rpP0n8iOtG87DdgQwJXXil_OpIVDrd-b3_1TjzuAYtXngmUawfvqi3Ql_VzL233HZN31SfKAtcXjCT4lcet4W-QN5YTuGRbpvlPjK-tAawtpJdvjO7OVkdlUfnNe8ZY1os8NYymoRdqt1H08SkOCjPjwSnUBlvSkZPY6lEbMUPqc7gx2KLM5914sq19XA2Pim1pG-_aLaeL4ITWwIh4LGRm_Sy34TjH7pQf5hBdq_tn6PRckDEpNzp-VugFxVvNcQYMa8HODEsKgqYipwSh0zXywpf6GRWEV7Dfp9Izyz7hKW1i1vq2Oq0E6rdO8qejlGoiI7e-Z4gql-i0Bm1RqfyG3pojHOa4C0twMuNt0oLQQNli1JjQNmtxxDbmBUwkQZriIjP7f0lLSxbPT8-1WYjT8qgXTFwfTk9S-v6-e-uLF8QuYhWZBHMOHUoNUttQhhfiGftoVQp7voIt4g0GFHEHd9YA-z-eh9OXBtr21_dbQNa9vIpAZQ3IC2PHwuvncCiXF7zf3PmhiIF3e9laPjGqW8lpKvvpzOeve6W1k66-F4OeALRwLQL5meVn4jEzhjWQx5qy-D0uUgV3HHsakeYVfjtrZn7HoUn3hTCzHxbMLDvHmsLzeOV4_3VeRPEJSk0_XMENwVzbtYO73Qfm5TQtbVi2xAE8TpnQ9vbTaIQXMn_XIZrBILOSGe-QQRzKxXJ5HhSMEro59KKlcz2ukOAdJqIOFZ_AidfyZCTJaO5sRKbXDlBc9pWPRVShalBCbqL2aNyfthh071vwPN3DMHBiUCl0r8oMFHUoieIRdrZ3X_jn5IJaMrCD9Ki0yiEIFAD6FJhBf-9GWrLnMoiNBa5ldH7b-d-rv1ESCAXiwRuEPkR2CmXnZtJQMX7uJ92G6EKdF8GiYD2jU1I8WByn3fsPdpyt59rkS3J5GuwUlZmmcBZcBY5T2MH3R3s4qHU0Kzn_XGwZMGGBympTmqNdUsZ4yMYdCveN3MvwhCyiWMFbEFvq5hw5FLDCDZSgscKPxeXXqhog0c-9D6vBGA_IM_mnXPYxqajpJ8RsJa315Pk_MxwSyeIEtj_dX0kCamebd1F4rm8fWWH7yxUtFlWSGRuXNOEtenplCTSxr1SOpFmaqZzmh3siKBJHi5oGEZqzwk2N4_mf_EsNMiQCIPexzaXZG5JO0f6TXSKc8w; OIDI=AhC7YSR9AilG9ExXCJaSIFIafj56sGho1i_nTs41VAwlWw; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=10.0.0&BRW=HTP&BRH=T&CW=962&CH=1014&SW=1920&SH=1080&DPR=1&UTC=480&DM=0&EXLTT=31&HV=1659406563&BZA=0",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77",
            "cvid": "1837B1DE4B4B4F598030DF19C4294FF7",
            "refig": "ce982d9c66944c0bbb9c97d930494ce2"
        }
        url = f"https://www.bing.com/search?q={parse.quote(question)}&count=50"
        try:
            Bing_response = requests.get(url, proxies=p, headers=headers)
        except:
            p = get_proxy()
            Bing_response = requests.get(url, proxies=p, headers=headers)

        try:
            self.question = self.question.replace("?", "")
            file_name = f"G:\QA\Webpages\{self.item_name}_{self.question}.html"
            soup = Bs(Bing_response.text, 'html.parser')
            ans = soup.find_all('ol')
            a = ""
            for i in ans:
                a += str(i)
            with open(file_name, "w", encoding="utf-8") as f1:
                f1.write(a)
                f1.close()

        except:
            element = 1


# 使用多线程获取页面
threadLock = threading.Lock()
global threads
threads = []


def get_info(stringarray, item_name):
    global threads
    for string in stringarray:
        thread = myThread(string, item_name)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    threads = []


back = ['', ' ', '是', '什么时候', '怎么', '在', '的', '得', '地', '什么', '哪',
            '有', '在哪', ' 英文', '品种', '价格', '作用', '时间', '地点', '为什么', '可以']


def run():
    T1 = time.perf_counter()
    t = T1
    flag = True
    with open(json_dir, encoding="utf-8") as json_file:
        attrbute = json.load(json_file)
        print("load json file success")
        T1 = time.perf_counter()
        t = T1
        entity = list(attrbute.keys())
        count = 0
        flag=True
        for item_name in entity:
            # if(flag):
            #     if(item_name!="60244_青岛"):
            #         continue
            #     flag=False
            #     continue
            if(count == 50):
                break
            count += 1
            key = list(attrbute[item_name].keys())
            string = []
            for j in key:
                questions = attrbute[item_name][j]
                for question in questions:
                    string.append(j+"_"+question[0])
            get_info(string, item_name)
            print(f"{item_name} done, time cost:{time.perf_counter()-T1}")
            T1 = time.perf_counter()
        print(f"time cost:{time.perf_counter()-t}")


if __name__ == "__main__":
    run()


# id_entity_中国地_中国地图全图高清版.html
