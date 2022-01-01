import pandas as pd

# Reading the csv file
df_new = pd.read_csv('../museum_csv.csv')

# saving xlsx file
xl = pd.ExcelWriter('museum_excel.xlsx')
df_new.to_excel(xl, index=False)

xl.save()
print("saving done")
xl.close()