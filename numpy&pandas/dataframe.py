import pandas as pd
import numpy as np

pf = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))
print(pf)