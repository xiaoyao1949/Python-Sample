import pandas as pd
import numpy as np

df=pd.DataFrame(np.arange(16).reshape(4,4),index=list("abcd"),columns=list("xyzn"))
print(df)
print(df.reindex(["a","j"]))

df2=df.set_index("x")
print(df2)

df3=df.set_index("x",drop=False)
print(df3)

df4=df.set_index(["x","y"],drop=False)
print(df4)
print(df4.index)
