import pandas as pd

data = pd.read_csv("employees.csv")
df = pd.DataFrame(data)

print("\n Filtering: \n")
print(df.loc[df['Age']>24])


print("\n Sorting: \n")
print(sorted(data['Age'], reverse=True))
print(df.sort_values(by=['First Name']))


print("\n Grouping: \n")
print(df.groupby('Age')['First Name'].count())