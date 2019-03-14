import pandas as pd
from pymysql import *
from pymongo import MongoClient

# 读取mysql
conn = connect(host = "127.0.0.1",port = 3306,user = "root",passwd ="mysql",db = "wobao",charset='gbk')
pf = pd.read_sql('select * from pabx',con=conn)
print(pf,type(pf))
pf.to_csv("平安保险_mysql.csv",index=False,encoding="gb18030")
conn.close()

# # 读取csv
# pf = pd.read_csv("../8.csv",encoding="gbk")

# 读取mongodb
client = MongoClient(host="127.0.0.1",port=27017)
# 链接数据库
db=client.book
#连接所用集合
collection = db.suning
#从mongodb获取数据
pf = pd.DataFrame(list(collection.find()))
pf.to_csv("苏宁_mongodb.csv",index=False,encoding="gb18030")
print(pf.head())
print(pf.tail())

# # 读取mongodb
# client = MongoClient() # 默认可以不传host和port,因为MongoClient已经默认设置好了
# #连接所用集合
# collection = client["book"]["suning"]
# #从mongodb获取数据
# data = list(collection.find())
# # print(data)
#
# pf=pd.Series(data)
# print(pf)
# t1 = pf[0]
#
# print(t1)

