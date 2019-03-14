"""
折线图
"""
from matplotlib import pyplot as plt

plt.figure(figsize=(20, 8), dpi=80)

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]
print(max(y), min(y))

# 绘制图形
plt.plot(x, y)

# 设置刻度密集度(整数)
# plt.xticks(range(2,25,2))

# 小数
_xticks_labels = [i / 2 for i in range(4, 49)]
plt.xticks(_xticks_labels[::3])

# 设置y轴刻度，对列表取最大值和最小值有max和min函数
plt.yticks(range(min(y), max(y) + 3, 2))

# 保存图片
plt.savefig('./1.svg')

# 展示图形
plt.show()
