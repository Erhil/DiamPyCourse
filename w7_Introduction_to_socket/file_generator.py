import numpy as np
import pandas as pd

data = np.random.beta(1, 100, (10000, 20))
df = pd.DataFrame(data)
df.to_csv("file_out.txt")