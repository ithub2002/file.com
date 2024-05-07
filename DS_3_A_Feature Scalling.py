from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
df = pd.DataFrame(data=data.data, columns=data.feature_names)
print("Original Dataset")
print(df.head())

scaler = MinMaxScaler()

df_scaled = scaler.fit_transform(df.to_numpy())
df_scaled = pd.DataFrame(df_scaled, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])

print("Scaled Dataset Using MinMaxScaler")
print(df_scaled.head())