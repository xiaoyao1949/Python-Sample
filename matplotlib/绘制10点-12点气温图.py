from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')

x = range(0,120)
y = [random.randint(20,35) for i in range(0,120)]

plt.figure(figsize=(20,8),dpi=80)


plt.plot(x,y)

# 横坐标如果只传一个参数，就必须是整数，如果想要有字符串，则必须传两个参数，并且要对应
# x = list(x)[::10]
# _xticks_labels=["hello{}".format(i) for i in x]
# plt.xticks(x,_xticks_labels)

# 两个列表相加
xtick_labels = ["10点{}分".format(i) for i in range(60)]
xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3],xtick_labels[::3],rotation=45,fontproperties=my_font)

plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 摄氏度",fontproperties=my_font)
plt.title("10点到12点气温变化情况",fontproperties=my_font)


plt.show()