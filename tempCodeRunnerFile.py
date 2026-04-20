import pandas as pd
Atif = pd.read_csv('dirtydata.csv')
x = Atif["Age"].mean()
Atif["Age"].fillna(x, inplace=True)
print(Atif.to_string())