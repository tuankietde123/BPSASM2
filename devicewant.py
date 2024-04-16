import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('DeviceWant.xlsx')

# View the first 5 rows
print("First 5 rows:")
print(df.head())

# View the last 5 rows
print("\nLast 5 rows:")
print(df.tail())


