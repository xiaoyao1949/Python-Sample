import numpy as np

t1 = np.arange(24).reshape(4,6)
print(t1)

t2 = np.where(t1<10,"a","b")  # 可以传字符串或者数字
print(t2)

print(t1)

t3 = t1.clip(10,18)           # 只能传数字
print(t3)


t4 = t3.astype(float)
t4[0,0] = np.nan
print(t4)