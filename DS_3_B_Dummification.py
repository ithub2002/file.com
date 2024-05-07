import pandas as pd

df = pd.DataFrame({'color': ['red', 'green', 'blue', 'red']})

df = pd.get_dummies(df, columns=['color'])

print(df)