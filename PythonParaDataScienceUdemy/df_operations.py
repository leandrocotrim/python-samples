# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 23:50:01 2018

@author: leandro.cotrim
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': [1,2,3,4], 'col2': [444,555,666,444], 'col3': ['abc','def','ghi', 'xyz']})
str_df = df.head()
print(str_df)
print()

df_u = df['col2'].unique()
print(df_u)
print()

df_u = np.unique(df['col2'])
print(df_u)
print()

df_n_u = df['col2'].nunique()
print(df_n_u)
print()

df_counts = df['col2'].value_counts()
print(df_counts)
print()


# Applay

def double(x):
    return x * 2

df_apply = df['col1'].apply(double)
print(df_apply)
print()

df_apply = df['col3'].apply(len)
print(df_apply)
print()

df_apply = df['col1'].apply(lambda x: x * x)
print(df_apply)
print()


# Columns
print(df.columns)
print()


# Indexs
print(df.index)
print()


# Sort
df_sort = df.sort_values('col2')
print(df_sort)
print()


# Is null
print(df.isnull())


# drop line contains nan
df_dropna = df.dropna()
print(df_dropna)
print()


print('#Fill item contains nan')
print()
df_fill_na = df['col1'].fillna(value=df['col1'].mean())
print(df_fill_na)
print()


print('#PIVOT')
print()
print(df)
print()

# Pivot table
df_pivot = df.pivot_table(values=['col1'], index=['col2', 'col3'])
print(df_pivot)
print()

df_pivot = pd.pivot_table(df, values=['col1', 'col3'], index=['col2'],
                          aggfunc='sum')
print(df_pivot)
print()




# Drop cols
# del df['col3']
# print(df)
# print()

# df.drop('col2')
# print(df)
# print()

