import selenium
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as Bs


def search(array):
    wd = webdriver.Chrome(r'E:\Chormedriver\chromedriver.exe')
    wd.get("https://www.google.com")
    wd.maximize_window()
    wait = WebDriverWait(wd, 50, 0.2)
    element = wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')))
    element.send_keys("1\n")

    element = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[3]/div[1]')))
    element.click()

    element = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')))
    back = ['', ' ', '是', '什么时候', '怎么', '在', '的', '得', '地', '什么', '哪',
            '有', '在哪', ' 英文', '品种', '价格', '作用', '时间', '地点', '为什么', '可以']
    ans = []
    number = array.__len__()
    entity_count = 0
    for string in array:
        question_count = 0
        for i in back:
            element.send_keys(string+i)
            element.click()
            time.sleep(0.5)
            # elements=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'sbct')))
            soup = Bs(wd.page_source, 'html.parser')
            list = soup.find_all('div', class_='wM6W7d')
            for i in list:
                if i.text not in ans:
                    ans.append(i.text)
                    question_count += 1
            temp_element = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[3]/div[1]')))
            temp_element.click()
        entity_count += 1
        if(entity_count%10==0):
            wd.close()
            wd = webdriver.Chrome(r'E:\Chormedriver\chromedriver.exe')
            wd.get("https://www.google.com")
            wd.maximize_window()
            wait = WebDriverWait(wd, 50, 0.2)
            element = wait.until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')))
            element.send_keys("1\n")
            element = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[3]/div[1]')))
            element.click()
            element = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')))

        print(str(entity_count*100/number)+"%  "+str(question_count))

    with open('Question.txt', 'w', encoding='utf-8') as f:
        for i in ans:
            if(i != ''):
                f.write(i+'\n')
    print(str(ans.__len__())+"questions have been found")
    wd.close()


# "杜甫","李白","卡丁车","游戏","韩国","盛大网络","橘子","金黄色","葡萄球菌","日本","父亲","中共中央党校","宣传部","浙江理工大学","计算机科学与技术","信息学院","亚运会","死神"
array = ['狂犬疫苗', "杜甫", "李白", "卡丁车", "游戏", "韩国", "盛大网络", "橘子", "金黄色", "葡萄球菌",
         "日本", "父亲", "中共中央党校", "宣传部", "浙江理工大学", "计算机科学与技术", "信息学院", "亚运会", "死神"]
search(array)
