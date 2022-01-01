import pandas as pd


# Reading the csv file
df_new = pd.read_csv('../museum_csv.csv')

# saving xml file
df_new.to_xml('museum_xml', index=False)

print("file created")
