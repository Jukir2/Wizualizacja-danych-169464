import numpy as np
import pandas as pd

# zad1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

# zad2
print(df[df['Liczba'] > 1000])
print(df[df['Imie'] == 'JAKUB'])
print(df.groupby(['Rok']).agg({'Liczba': ['sum']}))
