import pandas as pd

list_tables = ['janeiro','fevereiro','marco','abril']

for month in list_tables:
    print(month)
    readding_tables =  pd.read_excel(f'{month}.xlsx')
    print(readding_tables)






