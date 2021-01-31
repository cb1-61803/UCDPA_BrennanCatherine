import pandas as pd
import numpy as np
import matplotlib
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


outer_df =pd.merge(df_ed, df_hea, on='Year', how='outer')
print(outer_df.head)
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
