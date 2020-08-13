"""
Example script to convert multiple tweet JSON object (nested) into csv file

"""

import json
import pandas as pd


#Loading from json file of interest, reading it line by line
data = []
with open('example.json', encoding="utf8") as json_file:
    for line in json_file:
        try:
            data.append(json.loads(line))
        except:
            print('.')

#Normalizing original json with pandas in order to "fix" nested object
data_df = pd.json_normalize(data, max_level=5)

#Use this to keep only JSON fields of interest
data_df_new = data_df[['field_1','field_2']]


#Export data into csv format
data_df_new.to_csv('example.csv', sep = ';', line_terminator = '', encoding = 'utf-8')
