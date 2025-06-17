import pandas as pd


df = pd.read_csv('eggs.csv')
print(df.head())

df.to_csv('output.csv', index=False)
