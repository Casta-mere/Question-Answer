import json


def run():
    with open("info_dict.json", encoding="utf-8") as json_file, open("data.txt", "r", encoding="utf-8") as data_file, open("result.txt", "w", encoding="utf-8") as result_file:
        attrbute = json.load(json_file)
        print("load json file success")
        line = data_file.readline()
        while line:
            item_name = line.split(",")[0]
            item_id = line.split(",")[1].split("\n")[0]
            try:
                attr = attrbute[item_id]['basicInfo']
            except:
                result_file.write(line)
            line=data_file.readline()


def run_2():
    with open("data.txt", "r", encoding="utf-8") as data_file, open("result_2.txt", "w", encoding="utf-8") as result_file:
        ans=[]
        line = data_file.readline()
        while line:
            item_name = line.split(",")[0]
            item_id = line.split(",")[1].split("\n")[0]
            if(item_name not in ans):
                ans.append(item_name)
            else:
                result_file.write(line)
            line=data_file.readline()

def run_3():
    with open("data.txt", "r", encoding="utf-8") as data_file, open("result_3.txt", "w", encoding="utf-8") as result_file, open("result_4.txt", "w", encoding="utf-8") as result_file_2:
        ans=[]
        line = data_file.readline()
        while line:
            if(line not in ans):
                ans.append(line)
                result_file.write(line)
            else:   
                result_file_2.write(line)
            line=data_file.readline()
if __name__=="__main__":
    run()
    # run_2()
    # run_3()