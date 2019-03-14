from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyhbd.ttc')
plt.figure(figsize=(20,8),dpi=80)

x = range(1,32)
y3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

plt.scatter(x,y3,label="3月气温图")
plt.scatter(x,y10,label="10月气温图")

# _xticks_labels=x  # 直接是数字
_xticks_labels=["{}日".format(i) for i in x]  # 字符串加数字
plt.xticks(x,_xticks_labels,rotation=45,fontproperties=my_font)

# 设置y轴刻度
y = range(0,31,2)
_yticks_labels= ["{}".format(i) for i in y]  # 字符串加数字
plt.yticks(y,_yticks_labels,fontproperties=my_font)

# 设置图例
plt.legend(prop=my_font)

# 绘制网格
plt.grid(alpha=0.2,color="#cccccc")

# 设置标题
plt.xlabel("日期",fontproperties=my_font)
plt.ylabel("温度 摄氏度",fontproperties=my_font)
plt.title("3月和10月气温变化情况",fontproperties=my_font)


plt.show()