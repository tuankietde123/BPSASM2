import pandas as pd
df = pd.read_excel('ProductDescription.xlsx')

for x in df.index:
    if df.loc[x, "Unit Price"] > 1000:
        df.drop(x,inplace=True)
        
print(df.to_string())
