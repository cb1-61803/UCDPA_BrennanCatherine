import pandas as pd
from functools import reduce
import re
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
#from sklearn.cluster import kMeans

import requests
###response_API = requests.get('https://datastore.codeforiati.org/api/1/access/activity.csv?reporting-org=XM-DAC-21-1&reporting-org.type=10&start-date__gt=2015-01-01&end-date__lt=2020-12-31&stream=True')
###print(response_API.status_code) import requests
###response_API = requests.get('https://datastore.codeforiati.org/api/1/access/activity.csv?reporting-org=XM-DAC-21-1&reporting-org.type=10&start-date__gt=2015-01-01&end-date__lt=2020-12-31&stream=True')
###print(response_API.status_code)






df = pd.read_csv('Final_CRS_Data_2016.csv')
#print(df[14])
print(df.head())

#for column_name in df.columns:
    #print(column_name)
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

#desc = df['Short description / Project title'].tolist()
#desc1 = desc.str()
#desc = df['Short description / Project title'].apply(','.join)
#def list_to_string(d):
   #str_esc = ""
    #for element in d:
        #str_esc += element
   #return str_esc
#d = desc
#print(list_to_string(d))
#for item in desc:
    #str(item)
#str_esc = ""
#for x in desc1:
   # str_esc += '' + x
#print (str_esc)

#for reg in desc:
    #print('\n "### No. of Occurrences:" :')
    #print(len(re.findall("\w+\W\d+\W\d\d\s\w+\s\d+", reg))


#df_first_check = df.replace(to_replace= "\w+\W\d+\W\d\d\s\w+\s\d+", value = 'Civil Society', regex = True)#
#print(df_first_check.shape)


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
df16 = df16.astype('float64')
print(df16.head())
index16 = df16.index
print(len(index16))
print(df16.dtypes)
#countNaN= df16['purpose'].isna().sum
#print(countNaN)
#df161 = df16.replace(to_replace='\w*', value= NaN, regex=True)

df17 = pd.read_csv('purpose_17.csv')
df17['purpose'] = df17.astype('float64')
print(df17.head())
index17 = df17.index
print(len(index17))
print(df17.dtypes)

df18 = pd.read_csv('purpose_18.csv')
df18['purpose'] = df18.astype('int64')
print(df18.head())
index18 = df18.index
print(len(index18))
print(df18.dtypes)

df19 = pd.read_csv('purpose_19.csv')
df19['purpose'] = df19.astype('float64')
print(df19.head())
index19 = df19.index
print(len(index19))
print(df19.dtypes)

df20 = pd.read_csv('purpose_20.csv')
df20['purpose'] = df20.astype('float64')
print('\n###DF20 metadata:')
print(df20.head())
index20 = df20.index
datatype_20 = df20.dtypes
print(len(index20))
print(datatype_20)
#df20['purpose'] = pd.to_numeric(df20['purpose'])
print(datatype_20)

df_code_list = pd.read_csv('code_list.csv')
df_code_list['purpose'] = df_code_list['purpose'].astype('float64')
print('\n###Code List Head:')
print(df_code_list.head())
datatype_df_code_list = df_code_list.dtypes
print('\n###Code List Datatype:')
print(df_code_list.dtypes)
print(datatype_df_code_list)

###merge longest data with full code list###
df_code_list_20 = pd.merge(df_code_list, df20, how = 'left', on ="purpose")
print('\n### Merge 1 head:')
print(df_code_list_20.head())
for column_name in df_code_list_20.columns:
    print(column_name)

#print(df_code_list_20.index())

#df_code_list_1920 = pd.merge(df_code_list_20, df19, how = 'left', on ="purpose")

dataframes_16to20 = [df_code_list_20, df19, df18, df17, df16]

#df_16to20 = reduce(lamda, left, right : pd.merg(left, right, on = ['purpose'], how = 'outer'), dataframes_16to20)
df_16to20 = reduce(lambda left,right: pd.merge(left,right,on='purpose', how='left'), dataframes_16to20)
print('\n### Merge 16to20')
print(df_16to20.head())
for column_name in df_16to20.columns:
    print(column_name)

print('\n### base dataset')
df_16to20 = df_16to20.drop(columns =['DESCRIPTION', 'Clarifications / Additional notes on coverage']).copy()
df_16to20['purpose'] = df_code_list['purpose'].astype('str')

print(df_16to20.dtypes)

#df_16to20_draft2 = [['purpose', '2016', '2017' , '2018', '2019', '2020', 'DESCRIPTION']]

print('\n### number of rows with missing data')
print(df_16to20.isnull().any().sum())
###drop empty rows

df_16to20_minus_empty_rows = df_16to20.dropna(how='any', subset = ['2020','2019','2018','2017','2016'])
print(df_16to20_minus_empty_rows.head())
print('\n### new number of empty rows')
print(df_16to20_minus_empty_rows.isnull().any(axis = 0).sum())

df_16to20_amounts = df_16to20_minus_empty_rows.copy()


df_16to20_amounts['sector'] = df_16to20_amounts['purpose'].str[:2]
print(df_16to20_amounts)
for column_name in df_16to20_amounts.columns:
    print(column_name)

print(df_16to20_amounts.dtypes)
#df.plot(x='purpose', y='2020', kind = 'scatter')


df_gen_env = pd.read_csv('Gen_Env 15_20_DATA_2.csv')
print(df_gen_env)
for column_name in df_gen_env.columns:
    print(column_name)
print(df_gen_env.dtypes)

#df_gen_env = df_gen_env.iloc[:, : 7]
df_gen_env['year'] = df_gen_env['year'].astype(str)
df_gen_env['channel'] = df_gen_env['channel'].astype(str)
df_gen_env['purposecode'] = df_gen_env['purposecode'].astype(str)
df_gen_env['Sector'] = df_gen_env['Sector'].astype(str)
df_gen_env['gender'] = df_gen_env['gender'].astype('bool')
df_gen_env['environment'] = df_gen_env['environment'].astype('bool')

df_gen_env_cl = df_gen_env.dropna( axis = 1)
df_gen_env_clean = df_gen_env_cl.drop('int_channelcode', 1)
print('\n###df_gen_env_clean')
print(df_gen_env_clean.dtypes)
print(df_gen_env_clean.shape)
print(df_gen_env_clean.head)

df_gen_env_clean.plot(x='year', y= 'extended', kind= 'scatter')
plt.show()

#df_gen_env_clean.plot(x='Sector', y= 'extended', kind= 'scatter')
#plt.show()

df_gen_env_clean_19 = df.loc[df_gen_env_clean['year'].isin('2019')]
df_gen_env_clean_19.plot(x='Sector', y= 'extended', kind= 'scatter')
plt.show()
#sns.set_theme()
#gender_ext_sec = df_gen_env_clean.pivot('Sector', 'gen mark','extended')
#f, ax = plt.subplot(figsize=(9,6))
#sns.heatmap(gender_ext_sec, annot = True, fmt = 'd', linewidths = .5, ax=ax)
#plt.show()
#sns.set_theme(style = 'white')
#sns.relplot(x='gender', y = 'environment', hue = 'Sector', size = 'extended')
#plt.show()

#sns.catplot(x='year', y = 'extended', huge = 'gender', kind = 'swarm', data = df_gen_env_clean)
#plt.show()

#sns.violinplot(x= 'year', y = 'extended', data = df_gen_env_clean, inner = None)
#plt.show()

#sns.catplot(x= 'year', y = 'extended', data = df_gen_env_clean, Kind= 'bar' )
#plt.show()


#model = kMeans(n_clusters = 3)
#model.fit(arr)
#labels = model.predict(arr)
#print(labels)














