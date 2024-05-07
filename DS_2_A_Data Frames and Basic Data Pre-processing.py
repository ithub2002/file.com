import pandas as pd

data_csv = pd.read_csv('employees.csv')
print(data_csv)

data_json = pd.read_json('employees.json')
print(data_json)