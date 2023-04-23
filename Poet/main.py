import json
# dir="data/info_Baidu.json"
dir="data/info_Bing.json"
def run():
     with open(dir,"r", encoding="utf-8") as json_file:
        json_object = json.load(json_file)
        print("load json file success")
        names=list(json_object.keys())
        dict={}
        number=len(names)
        count=0
        for name in names:
            l=list(set(json_object[name]))
            for i in l:
                try:
                    if( "{" in i):
                        if(i not in list(dict.keys())):
                            # dict.update({i[0]:1})
                            dict[i]=1
                        else:
                            dict[i]+=1
                except:
                    element=1
            if(count%100==0):
                print(count/number)
            count+=1

        names=list(dict.keys())
        with open ("ans_bing_all.txt","w",encoding="utf-8")as f:
            for name in names:
                if(dict[name]>10):
                    # print(name)
                    f.write(name+"\n")

def run_2():
    with open(dir,"r",encoding="utf-8")as json_file:
        json_file=json.load(json_file)
        names=list(json_file.keys())
        dict={}
        number=len(names)
        count=0
        for name in names:
            l=list(set(json_file[name]))
            for i in l:
                try:
                    if (not i[0]=="{") and "{" in i:
                        if(i not in list(dict.keys())):
                            dict[i]=1
                        else:
                            dict[i]+=1
                except:
                    element=1
            if(count%100==0):
                print(count/number)
            count+=1
        names=list(dict.keys())
        with open ("ans_bing_2.txt","w",encoding="utf-8")as f:
            for name in names:
                if(dict[name]>=2):
                    f.write(name+"\n")

def run_3():
    ans=[]
    with open("ans.txt","r",encoding="utf-8") as f:
        line=f.readline()
        
        while line:
            ans.append(line.split("\n")[0])
            line=f.readline()
        ans=list(set(ans))
    with open("ans.txt","w",encoding="utf-8") as f:
        for i in ans:
            f.write(i+"\n")
    
if __name__ == '__main__':
    run_2()
    run()
    # run_3()