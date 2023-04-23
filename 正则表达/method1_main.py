'''
别名
诗人|的|被称为|别名|别称|有|是什么|什么|叫什么|之称
字
诗人|的|字|是什么|什么
号
诗人|的|号|是什么|什么
字号
诗人|的|字号|字和号|是什么|什么
本名
诗人|的|本名|原名|是什么|什么|叫什么
墓葬地
诗人|死后|的|陵墓|墓|墓地|墓葬地|墓冢|葬地|葬|埋|位于|在|哪里|哪儿|何处|什么地方|地址|所在地
去世地
诗人|死于|死在|在|是在|哪里|哪儿|何处|什么地方|死了|死的|死掉|逝世|去世|离世|亡故|辞世 
所处时代
诗人|生活在|是|属于|哪个|哪|什么|所在的|朝代|时期|朝|时候|的|是|人|诗人
主要作品
关于|诗人|有哪些|有什么|的|代表|著名|主要|有名|经典|诗句|诗|诗歌|诗词|作品|诗集|代表作|是什么|有哪些|有什么
主要成就
诗人|有什么|有哪些|的|个人|主要|文学|艺术|词史|成就|贡献|是什么|有什么|有哪些 
爵位
诗人|当过什么|有过什么|最高|的|爵位|是什么
官职
诗人|当时|一生|从事|有过|做过|当过|最大|最高|什么|官衔|官|职务|官职|官位|是|什么|几品
后世地位
诗人|对|在|的|世界上|后世|历史上|文学史上|文学|有怎样的|有哪些|有什么|的|影响|地位|有哪些|是什么|如何
谥号
诗人|被追赠|有|的|什么|谥号|叫什么|是什么
民族
诗人|是|的|什么|哪个|民族|的人|是什么
籍贯
诗人|的|籍贯|祖籍|在哪里|是什么 
逝世日期
诗人|是|在|的|什么时候|多会儿|哪年|哪一年|死|死掉|逝世|去世|离世|亡故|辞世|的|时间|日期|几月几日|年份 是|在|什么时候|多会儿|哪年
出生日期
诗人|是|在|的|什么时候|多会儿|哪年|哪一年|出生|的|时间|日期|几月几日|年份|是|在|什么时候|多会儿|哪年



条目类型
1 匹配单个且正确
2 匹配单个但错误
3 匹配多个
4 不在infobox
'''

import re


class poet:
    def __init__(self):
        self.rule = preload()

    def check(self, question):
        # 通过之前构造的规则，直接对示例进行匹配项，并对每一个规则中的匹配条目数量进行排序，取出匹配量最大的一条，认定为问题意图
        q = self.rule.keys()
        ret=""
        ans = []
        for i in q:
            ans.append([len(re.findall(i, question)), self.rule[i]])
        ans.sort(reverse=True)

        if(ans[0][0]!=ans[1][0]):
            st=question.strip("\n")+" ---- "+str(ans[0][1])
            print(st)
            ret+=st+"\n"
            print()
            return ret+"\n"
        return False

def preload():
    ans = {}
    with open("rules.txt", "r", encoding="utf-8") as f:
        i = f.readline()
        j = f.readline()
        while(i):
            ans.update({j.strip("\n"): i.strip("\n")})
            i = f.readline()
            j = f.readline()

    return ans

with open ("Question.txt","r",encoding="utf-8") as f, open("method1_ans.txt","w",encoding="utf-8") as g:
    p = poet()
    question = f.readline()
    while(question):
        ans = p.check(question)
        if(ans):
            g.write(ans)
        question = f.readline()
