from itertools import product

def show(a):
    ans=[""]
    for i in a:
        temp=list(product(ans,i))
        ans=[]
        for j in temp:
            ans.append(j[0]+j[1])    

    for i in ans:
        print(i)

poet=[]
When_Dynasty=[[],[],[]]
When_Dynasty[0].append("是")
When_Dynasty[0].append("属于")
# When_Dynasty[0].append("")
When_Dynasty[1].append("哪个")
When_Dynasty[1].append("哪")
When_Dynasty[1].append("什么")
# When_Dynasty[1].append("")

When_Dynasty[2].append("朝代")
When_Dynasty[2].append("时候")
When_Dynasty[2].append("时期")
When_Dynasty[2].append("朝")


show(When_Dynasty)

# res = list(product(When_Dynasty[i] for i in range(len(When_Dynasty))))