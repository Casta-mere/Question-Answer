# # 有"-"/"?"/"   "分隔的搜索条目
# ques=[]
# with open("que.txt","r",encoding="utf-8")as f:
#     ques=f.readlines()
# # print(ques)
# ques1=[]
# for q in ques:
#     if "来自百度百科" in q:
#         continue
#     elif "?" in q and "            " not in q:
#         ques1.append(q.split("?")[0])
#     if "-" in q:
#         ques1.append(q.split("-")[0])
#     elif "            " in q:
#         temp=q.split("            ")
#         for t in temp:
#             if t != "":
#                 ques1.append(t.strip(" "))
# print(ques1)

# with open("que1.txt","w",encoding="utf-8")as f:
#     for q in ques1:
#         if q!="\n" and q!="" and q!='\n' and q!="大家还在搜":
#             f.write(q+"\n")

# 二次清洗
ques=[]
with open("que1.txt","r",encoding="utf-8")as f:
    ques=f.readlines()
# print(ques)
ques1=[]
# print(ques.count("\n"))
# for i in range(13265):
#     ques.remove("\n")
    
for q in ques:
    if "?" in q and "            " not in q:
        q=q.split("?")[0]
    if "-" in q:
        q=q.split("-")[0]
    if "\n" in q:
        q=q.replace("\n","")
    if " " in q:
        q=q.split(" ")[0]
    # if "_" in q:
    #     q=q.split("_")[0]
    if q not in ques1:
        ques1.append(q)
# print(ques1)

with open("que2.txt","w",encoding="utf-8")as f:
    for q in ques1:
        if q!="\n" and q!="" and q!='\n' and q!="大家还在搜":
            f.write(q+"\n")
        