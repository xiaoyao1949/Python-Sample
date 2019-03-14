# coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)
print(type(df))
# print(df.head(1))
# print(df.info())

#rating,runtime分布情况
#选择图形，直方图
#准备数据
runtime_data = df["Rating"].values
print(type(runtime_data))
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

print(max_runtime,min_runtime)
#计算组数
num_bin_list = [1.9]

i=3.0
while i<=max_runtime:
    i += 0.5
    num_bin_list.append(i)


print(tuple(num_bin_list))
print(len(num_bin_list))
#设置图形的大小
plt.figure(figsize=(20,8),dpi=80)
plt.hist(runtime_data,num_bin_list)

# _x = [min_runtime]
# i = min_runtime
# while i<=max_runtime+0.5:
#     i = i+0.5
#     _x.append(i)

plt.xticks(num_bin_list)

plt.show()
