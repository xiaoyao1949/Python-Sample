import numpy as np
import random


t1 = np.array(range(5))
print(t1)

t2 = np.arange(5)
print(t2)

t4 = np.array(range(1,4),dtype=float)  # 指定数据类型

print(t4)
print(t4.dtype)

t7 = t4.astype("int64")
print(t7.dtype)

t5 = np.array([random.random() for i in range(10)])
print(t5)
print(t5.dtype)

t6 = np.round(t5,3)
print(t6)