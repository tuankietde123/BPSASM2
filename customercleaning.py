import pandas as pd
df = pd.read_excel('Customer Data.xlsx')

new_df = df.dropna()

print(new_df.to_string())