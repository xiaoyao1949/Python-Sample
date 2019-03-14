from matplotlib import pyplot as plt
import pandas

df = pandas.read_csv("./IMDB-Movie-Data.csv")
# print(df)
data_rate = df["Rating"].values
# print(data_rate,type(data_rate))

plt.figure(figsize=(20,8),dpi=80)
max = max(data_rate)
min = min(data_rate)
print(min,max,max-min)
num_bin = (max-min)//0.5
print(int(num_bin))

plt.hist(data_rate,int(num_bin))
print(min*10)

_x=list(range(int(min*10),int(max*10)+5,5))
print(_x)

_x=[i/10 for i in _x]
print(_x)
plt.xticks(_x)
plt.show()

