from urllib import response
import requests
import time
from bs4 import BeautifulSoup

def get_proxy():
    score = 1
    while score < 98:
        ip, score = requests.get(
            "http://10.11.195.12:1111/fetch").json()["proxy"]
    return {"http": f'http://{ip}'}

poets=[]
with open("res1.txt","r",encoding="utf-8") as f:
    ap=f.readlines()
    for p in ap:
        poets.append(p.split("\n")[0])

# infoback=['本名', '别名', '字', '号', '所处时代','出生日期','逝世日期', '主要作品',
#          '主要成就','去世地','墓葬地','爵位', '官职','后世地位','谥号','民族'
#          '', ' ', '是', '什么时候', '怎么', '在', '的', '得', '地', '什么', '哪',
#             '有', '在哪', ' 英文', '时间', '地点', '为什么', '可以']

infoback = ['简介','诗集','故乡','人物生平','文学特点','人物评价','轶事典故','后世影响','史书记载','年龄']

allText=[]
for word in infoback:
    for name in poets:
        search=name+word
        # time.sleep(0.5)
        url=f"https://www.baidu.com/s?wd={search}"
        headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'BIDUPSID=E3A99E52B8B012712AB6EFE89D870FD6; PSTM=1639726201; __yjs_duid=1_234adefb36a0c88196834acb4fa07eb21639728506413; BDUSS=ZVRzJoajFSS2lXS0NQb1Exd0w5N1RDTmFVdTFweG1hajJ-S0RFTlgtd25BbGhoSVFBQUFBJCQAAAAAAAAAAAEAAACWNLI~6s~KzbXbvKcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACd1MGEndTBhdT; BDUSS_BFESS=ZVRzJoajFSS2lXS0NQb1Exd0w5N1RDTmFVdTFweG1hajJ-S0RFTlgtd25BbGhoSVFBQUFBJCQAAAAAAAAAAAEAAACWNLI~6s~KzbXbvKcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACd1MGEndTBhdT; BD_UPN=12314753; BAIDUID=D8E5F16BDAF97A18B0BE8FAD90CEF30E:FG=1; H_WISE_SIDS=107311_110085_179350_180639_188740_194519_196428_197471_197711_199576_202012_204908_206122_208721_209204_209568_210322_210324_212295_212739_213034_213345_214109_214130_214137_214143_214790_215730_216212_216367_216851_216883_216941_217659_218445_218459_218478_218548_218597_219155_219244_219363_219451_219510_219666_219715_219731_219733_219842_219888_219942_219946_220067_220071_220277_220300_220315_220332_220344_220394_220607_220663_220896_221006_221016_221089_221108_221117_221118_221121_221307_221318_221385_221434_221502_221645_221795_221824_221842_221877_221919_221971_222135_222272_222392_222397_222417_222522_222615_222618_222619_222625; ispeed_lsm=2; H_WISE_SIDS_BFESS=107311_110085_179350_180639_188740_194519_196428_197471_197711_199576_202012_204908_206122_208721_209204_209568_210322_210324_212295_212739_213034_213345_214109_214130_214137_214143_214790_215730_216212_216367_216851_216883_216941_217659_218445_218459_218478_218548_218597_219155_219244_219363_219451_219510_219666_219715_219731_219733_219842_219888_219942_219946_220067_220071_220277_220300_220315_220332_220344_220394_220607_220663_220896_221006_221016_221089_221108_221117_221118_221121_221307_221318_221385_221434_221502_221645_221795_221824_221842_221877_221919_221971_222135_222272_222392_222397_222417_222522_222615_222618_222619_222625; BAIDUID_BFESS=44DDE0E51505CA43FF56FDF0DCFEDA49:FG=1; BA_HECTOR=24a1052lal208k8h252j7bad1hfgqvn16; ZFY=KSZjBELkHbc63kTdD:AqeuIm4TDZ76krw:BgfRdaIbL0E:C; RT="z=1&dm=baidu.com&si=lk2r8n90h9&ss=l6srplsr&sl=b&tt=4bh&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=23ti&cl=2460&ul=2hts&hd=2hup"; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=3; H_PS_PSSID=36560_36466_37115_37107_36413_37143_36955_34812_36917_37136_26350_36864_37022; sugstore=1; H_PS_645EC=cce9KQrZ0j4RGGxEHd8ZJlOBeGBcC14A0MnJxx%2BU1ChubgQovPVBsu3Dw%2Fg; baikeVisitId=db6427a5-bfc1-4d49-95aa-30cc81e81a7a; B64_BOT=1',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
                }
        res=requests.get(url=url,headers=headers)
        soup=BeautifulSoup(res.text,"html.parser")
        Text=soup.find_all('div',class_='c-container')
        
        for t in Text:
            temp=str(t.text).replace("\n","")
            if temp not in allText:
                allText.append(temp)
        # file=name+".html"
        
    print(name+"done.")
    
with open("what3.txt","a",encoding="utf-8")as f:
    for t in allText:
        f.write(str(t).replace("\ue62b\ue680播报\ue67d暂停","").replace("\ue636","").replace("\ue62b","").replace("\ue627","")+"\n")
        # f.write(res.text)    