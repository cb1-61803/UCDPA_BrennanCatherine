import pandas as pd
import re
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt


import requests
###response_API = requests.get('https://datastore.codeforiati.org/api/1/access/activity.csv?reporting-org=XM-DAC-21-1&reporting-org.type=10&start-date__gt=2015-01-01&end-date__lt=2020-12-31&stream=True')
###print(response_API.status_code) import requests
###response_API = requests.get('https://datastore.codeforiati.org/api/1/access/activity.csv?reporting-org=XM-DAC-21-1&reporting-org.type=10&start-date__gt=2015-01-01&end-date__lt=2020-12-31&stream=True')
###print(response_API.status_code)






df = pd.read_csv('Final_CRS_Data_2016.csv')
#print(df[14])
print(df.head())

for column_name in df.columns:
    print(column_name)
#print('The DataFrame is :\n', df)
#get dataframe shape
#shape = df.shape
#print('\nDataFrame Shape :', shape)
#print('\nNumber of rows :', shape[0])
#print('\nNumber of columns :', shape[1])
#Print the values of df
#print(df.values)
# Print the column index of df
#print(df.columns)
# Print the row index of df
#print(df.index)
###count num of TIMES

desc = df['Short description / Project title'].tolist()
def total_occur():
    for reg in desc:
        print(re.findall("\w+\W\d+\W\d\d\s\w+\s\d+", reg))


df_first_check = df.replace(to_replace= "\w+\W\d+\W\d\d\s\w+\s\d+", value = 'Civil Society', regex = True)
print(df_first_check.shape)


###VCSF.2012.10 Year
#string_check_df = df['CRS Identification N�', 'Short description / Project title'].copy(deep=True)
#(string_check_df.head())
#string_check_list = df.values.tolist(string_check_df)
#print(string_check_list)
#df[14].values.tolist()
#print()
#regex = r"\w+\W\d+\W\d\d\s\w+\s\d+"
#for element, item in check1:
    #if re.findall(regex,element):
        #print("correction required: {variable}".format(variable = string))

#target string =
#res_string = re,sub(r"", replace with, target_string)

df16 = pd.read_csv('purpose_16.csv')
df16['purpose'] = df16['purpose'].astype('int64')
print(df16.head())
index16 = df16.index
print(len(index16))
print(df16.dtypes)
#countNaN= df16['purpose'].isna().sum
#print(countNaN)
#df161 = df16.replace(to_replace='\w*', value= NaN, regex=True)

df17 = pd.read_csv('purpose_17.csv')
df17['purpose'] = df17['purpose'].astype('int64')
print(df17.head())
index17 = df17.index
print(len(index17))
print(df17.dtypes)

df18 = pd.read_csv('purpose_18.csv')
df18['purpose'] = df18['purpose'].astype('int64')
print(df18.head())
index18 = df18.index
print(len(index18))
print(df18.dtypes)

df19 = pd.read_csv('purpose_19.csv')
df19['purpose'] = df19['purpose'].astype('int64')
print(df19.head())
index19 = df19.index
print(len(index19))
print(df19.dtypes)

df20 = pd.read_csv('purpose_20.csv')
df20['purpose'] = df20['purpose'].astype('int64')
print('\n###DF20 metadata:')
print(df20.head())
index20 = df20.index
datatype_20 = df20.dtypes
print(len(index20))
print(datatype_20)
#df20['purpose'] = pd.to_numeric(df20['purpose'])
print(datatype_20)

df_code_list = pd.read_csv('code_list.csv')
df_code_list['purpose'] = df_code_list['purpose'].astype('int64')
datatype_df_code_list = df_code_list.dtypes
print('\n###Code List Head:')
print(df_code_list.head())
print('\n###Code List Datatype:')
print(datatype_df_code_list)

df_code_list_20 = pd.merge(df_code_list, df20, how = 'left', on ="purpose")
print('\n### Merge 1 head:')
print(df_code_list_20.head())
for column_name in df_code_list_20.columns:
    print(column_name)

index_df_code_list_20 = df_code_list_20.index
print(index_df_code_list_20)



