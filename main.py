import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

#import requests
#response = requests.get('https://stats.oecd.org/SDMX-JSON/data/TABLE5/20005+20001+801+1+2+301+68+3+18+4+5+40+75+20+21+6+701+742+22+7+820+8+76+9+69+61+50+10+11+12+302+20002+918+20013+958+20022+20016+913+914+20015+915+20014+909+1019+906+1013+990+976+20021+988+940+971+959+948+807+974+967+963+923+964+966+928+1023+20012+20033+901+905+903+20034+1012+953+921+1024+1025+1020+1011+1311+811+1312+1313+1016+104+951+978+20006+611+72+62+82+613+552+83+84+45+77+87+566+765+55+576+21600+1625+1609+1601+1613+1620+1614+1615+1617+1618+1627+1616+1626+1607+1612+1619+1606+1610+1605+1621+1611+1622+1628+1624+20035+1602+1604+1603.100+110+111+112+113+114+120+121+122+130+140+150+151+152+160+200+210+220+230+240+250+300+310+311+312+313+320+321+322+323+331+332+400+410+430+450+500+510+520+530+600+700+720+730+740+998+1000.528.A+D/all?startTime=2010&endTime=2019&dimensionAtObservation=allDimensions&pid=3dc299d4-abc8-4258-8355-456214a41e4f')
#print(response)


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
print(df.sort_values('Aid type'))
print(df.sort_values('Donor'))


df_don_sec_val_year = df[['Donor', "Sector", 'Value', 'Year','Amount type']]
print(df_don_sec_val_year.head())

df_ire = df_don_sec_val_year.loc[(df_don_sec_val_year["Donor"] == 'Ireland')]
#df_ire_1 = df_ire_at.drop_duplicates(subset ="Sector")
df_ire_1 = df_ire.loc[(df_ire["Amount type"] == 'Constant Prices')]
print(df_ire_1.head())
df_ire_sec = df_ire_1[["Sector", 'Value', 'Year']]

print("df_ire_sec = Clean Data Set")
print(df_ire_sec.head())
print(df_ire_sec.values)
print(df_ire_sec.shape)

print("df_ire_ed = Test for Education")
df_ire_ed = df_ire_sec.loc[(df_ire_sec["Sector"] == 'I.1. Education')]
print(df_ire_ed.head())
print(df_ire_ed.shape)

df_ed = df_ire_ed[['Value', 'Year']]
print(df_ed.head())
print(df_ed.shape)


df_hea = df_ire_sec.loc[(df_ire_sec["Sector"] == 'I.2. Health')]
df_pop = df_ire_sec.loc[(df_ire_sec["Sector"] == 'I.3. Population Policies/Programmes & Reproductive Health')]
df_watsan = df_ire_sec.loc[(df_ire_sec["Sector"] == 'I.4. Water Supply & Sanitation')]
df_gov = df_ire_sec.loc[(df_ire_sec["Sector"] == 'I.5. Government & Civil Society')]

df_infra = df_ire_sec.loc[(df_ire_sec["Sector"] == 'I.6. Other Social Infrastructure & Services')]

outer_df =pd.merge(df_ed, df_hea, on='Year', how='outer')
print(outer_df.head)
plt.show()

#clean df df_ire_sec sector value year

# Define a function
def sector(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)



fig, ax = plt.subplots()
sector(ax, df_ed["Year"], df_ed['Value'], 'blue', "Year", "USD millions")
ax2 = ax.twinx()
sector(ax2, df_pop["Year"], df_pop['Value'], 'red', "Year", "USD millions")
ax.set_title("Education and Population/Reproductive Health")
#plt.show()

# Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Plot year against value
ax.plot(df_ed["Year"], df_ed["Value"], color='b', marker='o', linestyle='--')
ax.plot(df_hea["Year"], df_hea["Value"], color='g', marker='o', linestyle='--')
ax.plot(df_pop["Year"], df_pop["Value"], color='r', marker='o', linestyle='--')
ax.plot(df_watsan["Year"], df_watsan["Value"], color='c', marker='o', linestyle='--')
ax.plot(df_gov["Year"], df_gov["Value"], color='y', marker='o', linestyle='--')
ax.plot(df_infra["Year"], df_infra["Value"], color='m', marker='o', linestyle='--')
ax.set_xlabel("Year")
ax.set_ylabel("US Dollar, Millions, 2018")
ax.set_title("Ireland's ODA to Social Infrastructure & Services")
ed = mpatches.Patch(color= 'b', label='Education')
hea = mpatches.Patch(color= 'g', label='Health')
pop = mpatches.Patch(color= 'r', label='Population')
watsan = mpatches.Patch(color= 'c', label='Water')
gov = mpatches.Patch(color= 'y', label='Governance')
infra = mpatches.Patch(color= 'm', label='Infrastructure')
plt.legend(handles=[ed, hea, pop, watsan, gov, infra], prop={'size': 6})

#plt.legend([df_ed, df_hea, df_pop, df_watsan, df_gov, df_infra],["Education", "Health", "Population", "Water", "Governance", "infrastructure"])
#ax.legend()

# figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(3, 2, sharey='all')
plt.legend(handles=[ed, hea, pop, watsan, gov, infra], prop={'size': 5},loc='upper right',)
ax[0, 0].plot(df_ed["Year"], df_ed["Value"], color='b', marker='o', linestyle='--',)
ax[0, 1].plot(df_hea["Year"], df_hea["Value"], color='g', marker='o', linestyle='--')
ax[1, 0].plot(df_pop["Year"], df_pop["Value"], color='r', marker='o', linestyle='--')
ax[1, 1].plot(df_watsan["Year"], df_watsan["Value"], color='c', marker='o', linestyle='--')
ax[2, 0].plot(df_gov["Year"], df_gov["Value"], color='y', marker='o', linestyle='--')
ax[2, 1].plot(df_infra["Year"], df_infra["Value"], color='m', marker='o', linestyle='--')

plt.show()

