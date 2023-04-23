from bs4 import BeautifulSoup as Bs

source="temp.txt"

with open(source, 'r', encoding='utf-8')as f, open("temp1.txt",'w',encoding='utf-8')as f1:
    lines=f.readlines()
    for line in lines:
        if("context" in line):
            f1.write(str(line).split('"context": "')[1])