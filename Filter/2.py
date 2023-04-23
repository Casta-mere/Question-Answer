filter = []
with open("ans.txt", "r", encoding="utf-8") as f:
    ap = f.readlines()
    for p in ap:
        # print(p.split(" ")[1])
        if p.split(" ")[1] != "not":
            filter.append(p.split("\n")[0])
    # print(ap)
print(filter)

# with open("res.txt","w",encoding="utf-8")as f:
#     for i in filter:
#         f.write(i+"\n")   

with open("res2.txt","w",encoding="utf-8")as f:
    for i in filter:
        f.write(i.split(" ")[0]+"\n")  