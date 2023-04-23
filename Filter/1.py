import selenium
import time
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as Bs


url="https://index.baidu.com/v2/index.html#/"


def search():
    wd = webdriver.Chrome(r'E:\Chormedriver\chromedriver.exe')
    wd.get(url)
    time.sleep(20)
    poets=[]
    with open("Poets.txt", "r", encoding="utf-8") as f:
        ap = f.readlines()
        for p in ap:
            poets.append(p.split("\n")[0])  
    wd.maximize_window()
    wait = WebDriverWait(wd, 50, 0.2)
    wait2 = WebDriverWait(wd, 1, 0.2)
    
    count=0
    with open("ans.txt","a",encoding="utf-8") as f:
        for i in poets:
            try:
                element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="search-input-form"]/input[3]')))
                element.send_keys(i+"\n")

                element = wait2.until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div')))
                f.write(i+" "+str(element.text)+"\n")
                element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div[1]')))
                element.click()
            except:
                f.write(i+" not found\n")
                element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div[1]')))
                element.click()
            os.system("cls")
            print(count/len(poets)*100,"%")
            count+=1

if __name__ == "__main__":
    search()
