"""
电影条形图
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc')
plt.figure(figsize=(20, 10), dpi=80)

a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5\n：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5\n：死无对证", "金刚：骷髅岛", "极限特工\n：终极回归",
     "生化危机6\n：终章", "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3\n：殊死一战", "蜘蛛侠\n：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]

b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
     6.86, 6.58, 6.23]
x = range(len(a))
x = [i + 1 for i in x]
y = b

plt.barh(x, y, height=0.5, left=0, color="orange")
plt.yticks(x, a, rotation=0, fontproperties=my_font)

# 设置图例
# plt.legend(prop=my_font)

# 绘制网格
plt.grid(alpha=0.2, color="#cccccc")

# 设置标题
plt.ylabel("电影", fontproperties=my_font)
plt.xlabel("评分", fontproperties=my_font)
plt.title("电影和评分条形图", fontproperties=my_font)

plt.show()
