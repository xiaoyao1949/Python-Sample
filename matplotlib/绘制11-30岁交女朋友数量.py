from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyhbd.ttc')
plt.figure(figsize=(20,8),dpi=80)

x = range(11,31)
y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]


plt.plot(x,y1,label="自己",color="k",linestyle="--")
plt.plot(x,y2,label="同桌",color='#fe4578',linewidth=2)

_xticks_label = ["{}岁".format(i) for i in x]
plt.xticks(x,_xticks_label,rotation=45,fontproperties=my_font)
plt.yticks(range(0,9))

# 绘制网格
plt.grid(alpha=0.1)

# 显示图例
plt.legend(prop=my_font,loc="best")

plt.show()
