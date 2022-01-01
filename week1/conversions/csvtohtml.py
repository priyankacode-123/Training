import pandas as pd

# reading csv
htm = pd.read_csv('../museum_csv.csv')
# converting to html
htm.to_html('museum.html')

print('file created')
