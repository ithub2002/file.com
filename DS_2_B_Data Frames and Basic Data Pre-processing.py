import pandas as pd
import numpy as np

dict = {
    "First Score": [100, 90, np.nan, 95],
    "Second Score": [30, 45, 56, np.nan],
    "Third Score": [np.nan, 40, 80, 98],
}

df = pd.DataFrame(dict)

print('\n Handling Missing Values \n')
print(df.isnull())
df = df.fillna(0)
print(df)

print('\n Handling Outliers \n')
df = df[df.apply(lambda x: np.abs((x - x.mean()) / x.std()) < 3).all(axis=1)]
print(df)
