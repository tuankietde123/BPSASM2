import pandas as pd

df = pd.read_excel('TrendTable.xlsx')

df.drop_duplicates(inplace=True)

print(df.to_string(index=False))