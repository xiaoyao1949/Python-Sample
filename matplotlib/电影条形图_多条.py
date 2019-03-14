from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyhbd.ttc')
plt.figure(figsize=(20,8),dpi=80)

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

width_bar=0.2

x_14 = list(range(len(a)))     # 转成数字列表x = range(len(x))
x_15 = [i+width_bar for i in x_14]  # 数字加步长
x_16 = [i+width_bar*2 for i in x_14]
print(x_14,x_15,x_16)

plt.bar(x_14,b_14,width=width_bar,color="orange",label='14日')
plt.bar(x_15,b_15,width=width_bar,color="green",label='15日')
plt.bar(x_16,b_16,width=width_bar,color="pink",label='16日')


plt.xticks(x_15,a,rotation=0,fontproperties=my_font)  #这里的xticks设置的是x_15,则中间的刻度就指向中间的

# 设置图例
plt.legend(prop=my_font)

# 绘制网格
plt.grid(alpha=0.2,color="#cccccc")

# 设置标题
plt.xlabel("电影",fontproperties=my_font)
plt.ylabel("评分",fontproperties=my_font)
plt.title("电影和评分条形图",fontproperties=my_font)


plt.show()