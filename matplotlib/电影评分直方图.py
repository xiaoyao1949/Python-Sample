"""
直方图
"""
from matplotlib import pyplot as plt
import pandas

df = pandas.read_csv("./IMDB-Movie-Data.csv")
# print(df)
data_rate = df["Rating"].values
print(len(data_rate))
print(data_rate, type(data_rate))

plt.figure(figsize=(20, 8), dpi=80)
max = max(data_rate)
min = min(data_rate)
print(min, max, max - min)
num_bin = (max - min) // 0.5
print(int(num_bin))

plt.hist(data_rate, int(num_bin))

_x = [min]
i = min
while i <= max + 0.5:
    i += 0.5
    _x.append(i)
print(_x)
plt.xticks(_x)
plt.show()
