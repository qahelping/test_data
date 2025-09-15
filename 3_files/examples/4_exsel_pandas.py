import pandas as pd

from files.files import EXCEL_FILE_PATH

# Чтение
df = pd.read_excel(EXCEL_FILE_PATH, sheet_name='Блоги')

print(df)
# Запись
df.to_excel('output.xlsx', sheet_name='Data', index=False)