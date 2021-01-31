import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('don_sector_10year.csv')
for column_name in df.columns:
    print(column_name)
print('The DataFrame is :\n', df)
#get dataframe shape
shape = df.shape
print('\nDataFrame Shape :', shape)
print('\nNumber of rows :', shape[0])
print('\nNumber of columns :', shape[1])
#Print the values of df
print(df.values)
# Print the column index of df
print(df.columns)
# Print the row index of df
print(df.index)
# Sort by Aid type
df_at = df.sort_values('Aid type')
print(df_at.head())
df_don = df.sort_values('Donor')
print(df_don.head())
df_don_sec_val_year = df[['Donor', "Sector", 'Value', 'Year','Amount type']]
print(df_don_sec_val_year.head())
#Ireland DONOR = 21
df_ire = df_don_sec_val_year.loc[(df_don_sec_val_year["Donor"] == 'Ireland')]
df_ire_1 = df_ire.loc[(df_ire["Amount type"] == 'Constant Prices')]
print(df_ire_1.head())
df_ire_sec = df_ire_1[[ "Sector", 'Value', 'Year']]
print("df_ire_sec = Clean Data Set")
print(df_ire_sec.values)
print(df_ire_sec.shape)
print("df_ire_ed = Test for Education")
df_ire_ed = df_ire_sec.loc[(df_ire_sec["Sector"] == 'I.1. Education')]

print(df_ire_ed.head())
print(df_ire_ed.shape)
df_ed = df_ire_ed[['Value', 'Year']]
print(df_ed.head())
print(df_ed.shape)
#print('function for recreating DFs')
df_hea = df_ire_sec.loc[(df_ire_sec ["Sector"] == 'I.2. Health')]
df_pop = df_ire_sec.loc[(df_ire_sec ["Sector"] == 'I.3. Population Policies/Programmes & Reproductive Health')]
df_watsan = df_ire_sec.loc[(df_ire_sec ["Sector"] == 'I.4. Water Supply & Sanitation')]
df_gov = df_ire_sec.loc[(df_ire_sec ["Sector"] == 'I.5. Government & Civil Society')]
df_infra = df_ire_sec.loc[(df_ire_sec ["Sector"] == 'I.6. Other Social Infrastructure & Services')]



fig, ax = plt.subplots()
ax.plot(df_ed["Year"], df_ed["Value"])
# Customize the x-axis label
ax.set_xlabel("Year")
# Customize the y-axis label
ax.set_ylabel("USD (million)")
# Add the title
ax.set_title("Ireland's ODA contribution to Education")
plt.show()

fig, ax = plt.subplots()
ax.plot(df_hea["Year"], df_hea["Value"])
# Customize the x-axis label
ax.set_xlabel("Year")
# Customize the y-axis label
ax.set_ylabel("USD (million)")
# Add the title
ax.set_title("Ireland's ODA contribution to Health")
plt.show()