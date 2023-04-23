# https://index.baidu.com/v2/main/index.html#/trend/%E6%9D%8E%E7%99%BD?words=%E6%9D%8E%E7%99%BD
from urllib import response
import requests
import time
from bs4 import BeautifulSoup
from urllib import parse

def get_proxy():
    score = 1
    while score < 98:
        ip, score = requests.get(
            "http://10.11.195.12:1111/fetch").json()["proxy"]
    return {"http": f'http://{ip}'}


poets = []
with open("Poets.txt", "r", encoding="utf-8") as f:
    ap = f.readlines()
    for p in ap:
        poets.append(p.split("\n")[0])

# for name in poets:
    # time.sleep(0.5)
name = "李白"
# url = f"https://index.baidu.com/v2/main/index.html#/trend/{name}?words={name}"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'BIDUPSID=E3A99E52B8B012712AB6EFE89D870FD6; PSTM=1639726201; __yjs_duid=1_234adefb36a0c88196834acb4fa07eb21639728506413; BDUSS=ZVRzJoajFSS2lXS0NQb1Exd0w5N1RDTmFVdTFweG1hajJ-S0RFTlgtd25BbGhoSVFBQUFBJCQAAAAAAAAAAAEAAACWNLI~6s~KzbXbvKcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACd1MGEndTBhdT; BAIDUID=D8E5F16BDAF97A18B0BE8FAD90CEF30E:FG=1; H_WISE_SIDS=107311_110085_179350_180639_188740_194519_196428_197471_197711_199576_202012_204908_206122_208721_209204_209568_210322_210324_212295_212739_213034_213345_214109_214130_214137_214143_214790_215730_216212_216367_216851_216883_216941_217659_218445_218459_218478_218548_218597_219155_219244_219363_219451_219510_219666_219715_219731_219733_219842_219888_219942_219946_220067_220071_220277_220300_220315_220332_220344_220394_220607_220663_220896_221006_221016_221089_221108_221117_221118_221121_221307_221318_221385_221434_221502_221645_221795_221824_221842_221877_221919_221971_222135_222272_222392_222397_222417_222522_222615_222618_222619_222625; H_WISE_SIDS_BFESS=107311_110085_179350_180639_188740_194519_196428_197471_197711_199576_202012_204908_206122_208721_209204_209568_210322_210324_212295_212739_213034_213345_214109_214130_214137_214143_214790_215730_216212_216367_216851_216883_216941_217659_218445_218459_218478_218548_218597_219155_219244_219363_219451_219510_219666_219715_219731_219733_219842_219888_219942_219946_220067_220071_220277_220300_220315_220332_220344_220394_220607_220663_220896_221006_221016_221089_221108_221117_221118_221121_221307_221318_221385_221434_221502_221645_221795_221824_221842_221877_221919_221971_222135_222272_222392_222397_222417_222522_222615_222618_222619_222625; ZFY=W2SGYQfslsSVUuJBlEAOXbVD7W:Bz:AXkyPiebsxlgqvc:C; BAIDUID_BFESS=D8E5F16BDAF97A18B0BE8FAD90CEF30E:FG=1; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1661738403; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%221068643478%22%2C%22scope%22%3A1%7D%7D; bdindexid=5btf5qg39tdpagov9rqu9pgrs1; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a041175085773WHU8Qx%2B%2FLDtJ%2FX%2Fk98F1qU5ks01IntDATQ2QfMLXXe8WjXlLpSiQMCvDmGCJrbzLrq8vxIkmj8giN12rYtxS8AzQiBS0Tp5l%2BZQx1jp9aTiYiQv5jReEZgvNlvw7U91f7wB6%2BiFVxlKc9YU2tmdg2hxs3A9JaV7zG7ET8Q7SAX4hfV4eq0T8fBLy1buOB8kdYhJx4lM63ksz4AW9sdYJLWdRixvyT4jiiIEMcSZebzzG%2BLljz4m8irkZRDxNYsEXGZllgb3mOtdOxRwGHJqNfotOYB0c5VUkHGFwB7l9TYW0r%2FlGOq3M3XHRxva2sFy94546775236736645897603051050640; __cas__rn__=411750857; __cas__st__212=d7ea304b718d894480c670ec517b0e869829b632063085191feec50cb20ada7afb88a50711c11014aa058abb; __cas__id__212=42058034; CPID_212=42058034; CPTK_212=1511868171; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1661740267; BDUSS_BFESS=ZVRzJoajFSS2lXS0NQb1Exd0w5N1RDTmFVdTFweG1hajJ-S0RFTlgtd25BbGhoSVFBQUFBJCQAAAAAAAAAAAEAAACWNLI~6s~KzbXbvKcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACd1MGEndTBhdT; ab_sr=1.0.1_NmQ2NmRlODM1OWNjN2VhMzg3NDIyMjllOTViNDJiYTNkZjRkYmQ5Yzg4YWYwYjg2MzQ5MTRiMWU1ZjI2MTY5MGZlYzYzMTdhODdmYWNkNzZlY2RkNjhlNTRiZGQyM2EzY2E2MjhlMzE4ZmRkYjQ3YzdjMzEwYjgxMDM2NzE1MzI1MjU2OWU5NzI1Nzg4MDc4OGZhMGFhN2FmMDY5MDQzOA==; RT="z=1&dm=baidu.com&si=96fc4110-896b-4ad2-a2a6-e0fa090ea51e&ss=l7e44yb8&sl=g&tt=ugw&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=148nn&ul=14cm4"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
name=parse.quote(name).replace('%', '%25')
# url=f"https://index.baidu.com/api/Route?fromu=https%3A%2F%2Findex.baidu.com%2Fv2%2Fmain%2Findex.html%23%2Ftrend%2F{name}%3Fwords%3D{name}"
url=f"https://index.baidu.com/api/Route?fromu=https://index.baidu.com/v2/main/index.html#/trend/{name}?words={name}"



res = requests.get(url=url, headers=headers)
print(res)
with open("res.html", "w", encoding="utf-8")as f:
    f.write(res.text)

# soup=BeautifulSoup(res.text,"html.parser")
# Text=soup.find_all('div',class_='veui-table-cell')
# print(Text)
# allText=[]
# for t in Text:
#     temp=str(t.text).replace("\n","")
#     if temp not in allText:
#         allText.append(temp)
# # file=name+".html"
# with open("what3.txt","a",encoding="utf-8")as f:
#     for t in allText:
#         f.write(str(t).replace("\ue62b\ue680播报\ue67d暂停","").replace("\ue636","").replace("\ue62b","").replace("\ue627","")+"\n")
#         # f.write(res.text)
# print(name+"done.")
