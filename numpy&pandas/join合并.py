import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4)),index=list("abc"),columns=list("xyzm"))

df2 = pd.DataFrame(np.zeros((2,4)),index=["a","b"],columns=list("ijkn"))

print(df1,"\n")
print(df2)
df3=df1.join(df2)
df4=df2.join(df1)
print(df3,"\n")
print(df4)

