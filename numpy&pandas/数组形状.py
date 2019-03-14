import numpy as np

t1 = np.arange(24).reshape(2,3,4)
print(t1)
t2=t1.reshape(6,4)
print(t2)
print(t2.shape)

t3 = t2.flatten()
print(t3)

t4 = np.arange(4).reshape(1,4)
print(t4)

print(t2-t4)