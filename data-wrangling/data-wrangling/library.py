import pandas as pd
import numpy as np

df = pd.read_csv('Library_Usage.csv')

# print(df.shape)
# print(df.info())
# print(df.head(5))

# print(df.describe())
# print(df.mean())
# print(df.max())
# print(df['Total Renewals'].min())
# print(df['Total Renewals'].mode())

def find_above_av_checkouts():
    av = df['Total Checkouts'].mean()
    av = av.round()
    return df[ df['Total Checkouts'] > av]

# print(find_above_av_checkouts())

def sort_by_home_library():
    columns = df[['Home Library Definition', 'Total Renewals', 'Patron Type Code', 'Total Checkouts']]
    return columns.sort_values(by='Home Library Definition', ascending=True)

# print(sort_by_home_library())

# print(df.isnull())

renewals = df['Total Renewals']
q1 = renewals.quantile(.25)
q3 = renewals.quantile(.75)
iqr = q3 - q1
pmin = q1 - 1.5 * iqr
pmax = q3 + 1.5 * iqr
new_renw = renewals[renewals.between(pmin, pmax)]
# print(new_renw)

# print(df.stack())

# df.reset_index().rename(columns={'index' : 'id'})
# print(df.melt(id_vars='id'))