import pandas as pd

# Чтение
df = pd.read_csv('data.csv')
print(df.head())  # Первые 5 строк

# Запись
df.to_csv('output.csv', index=False)