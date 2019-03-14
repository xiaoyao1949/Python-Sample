import pandas as pd
from pymysql import *
from pymongo import MongoClient

# 读取mongodb
client = MongoClient(host="127.0.0.1",port=27017)
# 链接数据库
db=client.book
#连接所用集合
collection = db.suning
#从mongodb获取数据
data = list(collection.find())
item_list=[]
for i in data:
    dict={}
    dict["b_cate"]=i["b_cate"]
    dict["book_author"]=i["book_author"]
    dict["book_press"]=i["book_press"]
    item_list.append(dict)
pf=pd.DataFrame(item_list)
# print(pf)
# print(pf[:10],"\r\n")
# print(pf["book_author"],"\r\n")

# item1 = pf.loc[2]["book_press"]
# print(item1)
# print(type(item1))

item2 = pf.loc[[4,2]]
print(pf)
print(item2)
print(type(item2))
# print(len(set(pf["b_cate"].tolist())))
print(type(pf["b_cate"]))



