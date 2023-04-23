import pymysql
import requests as req
import time as t

def Create_D(name):
    conn=pymysql.connect(host='localhost',user='root',password='',charset='utf8')
    cursor=conn.cursor()
    sql=f"DROP database IF EXISTS `{name}`;"
    cursor.execute(sql)
    sql=f"create database `{name}`;"
    cursor.execute(sql)
    cursor.close()
    conn.close()

def drop_table(table):
    conn=pymysql.connect(host='localhost',user='root',password='',db='QuestionAnswer',charset='utf8')
    cursor=conn.cursor()
    sql=f"DROP table IF EXISTS `{table}`;"
    cursor.execute(sql)
    cursor.close()

def create_table(table):
    drop_table(table)
    conn=pymysql.connect(host='localhost',user='root',password='',db='QuestionAnswer',charset='utf8')
    cursor=conn.cursor()
    sql=f"DROP table IF EXISTS `{table}`;"
    cursor.execute(sql)
    sql=f"create Table `{table}`(id int,name varchar(100))"
    cursor.execute(sql)
    cursor.close()

conn=pymysql.connect(host='localhost',user='root',password='',db='QuestionAnswer',charset='utf8')
cursor=conn.cursor()
def up_Sql(List,table):
    sql=f'insert into `{table}` values("{List[0]}","{List[1]}");'
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    

resource="all_entitiestxt"
ans="ans.txt"

if __name__ == '__main__':
    # Create_D("BaiduBaike_data")
    create_table("BaiduBaike_data_2")
    with open(resource,'r',encoding="utf-8") as f:
        lines=f.readlines()
        i=0
        T1 = t.perf_counter()
        for line in lines:
            List=line.split('\t')
            up_Sql(List,'BaiduBaike_data_2')
            i+=1
            if(i%10000==0):
                print(i/10000,end=' ')
                print(t.perf_counter()-T1)
                T1=t.perf_counter()
    cursor.close()
    conn.close()
    