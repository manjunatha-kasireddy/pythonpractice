import pandas as pd

df = pd.read_csv('data.csv')

print(df) 
df = pd.read_csv('data.csv')

print(df.head(10))
print(df.head())
print(df.tail())
print(df.info())

new_df = df.dropna()

print(new_df.to_string())

