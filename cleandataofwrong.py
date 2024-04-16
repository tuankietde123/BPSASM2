import pandas as pd
df = pd.read_excel('SaleTable.xlsx')

df['Sale Date'] = pd.to_datetime(df['Sale Date'])

df.dropna(subset=['Sale Date'], inplace=True)

print(df.to_string())
