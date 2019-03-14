import pandas as pd
import numpy as np

df = pd.read_csv("./starbucks_store_worldwide.csv")
country = df.groupby(by="Country")
# print(country)
# for i,j in country:
#     print(i,type(i))
#     print("*"*100)
#     print(j,type(j))
#     print("-"*100)

print(country["City"].count())  # 根据国家，每一列的数据都统计个数
country_count =  (country["City"]).count()
print(type(country_count))
print(country_count["US"],type(country_count["US"]))
print(country_count["ZA"])

zh = df[df["Country"]=="CN"]
print(zh)
zh_count=zh.groupby(by="State/Province").count()[["Brand"]]
print(zh_count,type(zh_count))

# 数据按照多个条件进行分组,返回Series
grouped = df.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]
print(grouped)
print(type(grouped))






