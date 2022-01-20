import requests
import pandas as pd
import json

# requesting museum API call for object values
my_req = requests.get(url="https://collectionapi.metmuseum.org/public/collection/v1/objects")
var = my_req.json()  # calling the JSON data

userdata = []

# collecting JSON data for each object
for i in var['objectIDs'][:20]:
    detail = requests.get(url="https://collectionapi.metmuseum.org/public/collection/v1/objects/{}".format(i))
    data = detail.json()
    userdata.append(data)  # appending in a empty list

# converting into pandas dataframes
df = pd.DataFrame(userdata)

# locating the columns to flatten the data
loc_to = df.loc[:, ['additionalImages', 'constituents', 'measurements', 'tags']]
for i in loc_to.columns:
    loc_to = loc_to.explode(i)

final_dict = pd.json_normalize(
    json.loads(loc_to.to_json(orient="records")))  # calling normalize function to flatten the data

df1 = pd.concat([df, final_dict], axis=1)

df1 = df1.drop(['additionalImages', 'constituents', 'measurements', 'tags'], axis=1)  # dropping off original columns

# converting dataframes into csv
df1.to_csv('museum_csv_with20_records.csv', index=False)
