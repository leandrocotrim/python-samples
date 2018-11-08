# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:17:12 2018

@author: leandro.cotrim
"""

import pandas as pd

# concat

df_1 = pd.DataFrame({ 'A' : ['A0', 'A1', 'A2', 'A3'],
                      'B' : ['B0', 'B1', 'B2', 'B3'],
                      'C' : ['C0', 'C1', 'C2', 'C3'],
                      'D' : ['D0', 'D1', 'D2', 'D3']
                    }, index=[0, 1, 2, 3])

df_2 = pd.DataFrame({ 'A' : ['A4', 'A5', 'A6', 'A7'],
                      'B' : ['B4', 'B5', 'B6', 'B7'],
                      'C' : ['C4', 'C5', 'C6', 'C7'],
                      'D' : ['D4', 'D5', 'D6', 'D7']
                    }, index=[4, 5, 6, 7])

df_3 = pd.DataFrame({ 'A' : ['A8', 'A9', 'A10', 'A11'],
                      'B' : ['B8', 'B9', 'B10', 'B11'],
                      'C' : ['C8', 'C9', 'C10', 'C11'],
                      'D' : ['D8', 'D9', 'D10', 'D11']
                    }, index=[8, 9, 10, 11])

# print dataFrames
print(df_1)
print(df_2)
print(df_3)
print()

# concat indexs 'rows'
df_concat = pd.concat([df_1, df_2, df_3])
print(df_concat)
print()

# concat columns 
df_concat = pd.concat([df_1, df_2, df_3], axis=1)
print(df_concat)
print()


# merge with single key

df_left = pd.DataFrame({ 'A' : ['A0', 'A1', 'A2', 'A3'],
                         'B' : ['B0', 'B1', 'B2', 'B3'],
                         'Key' : ['K0', 'K1', 'K2', 'K3']
                       }, index=[0, 1, 2, 3])

df_right = pd.DataFrame({ 'C' : ['C0', 'C1', 'C2', 'C3'],
                          'D' : ['D0', 'D1', 'D2', 'D3'],
                          'Key' : ['K0', 'K1', 'K2', 'K3']
                        }, index=[0, 1, 2, 3])

df_merge = pd.merge(df_left, df_right, how="inner", on="Key")
print(df_merge)
print()


# merge with dooble key

df_left = pd.DataFrame({ 'Key1' : ['K0', 'K0', 'K1', 'K2'],
                         'Key2' : ['K0', 'K1', 'K0', 'K1'],
                         'A' : ['A0', 'A1', 'A2', 'A3'],
                         'B' : ['B0', 'B1', 'B2', 'B3']
                       })

df_right = pd.DataFrame({ 'Key1' : ['K0', 'K1', 'K1', 'K2'],
                          'Key2' : ['K0', 'K0', 'K0', 'K0'],
                          'C' : ['C0', 'C1', 'C2', 'C3'],
                          'D' : ['D0', 'D1', 'D2', 'D3']
                       })
# print dataFrames
print(df_left)
print(df_right)
print()

# merger inner
df_merge_inner = pd.merge(df_left, df_right, on=['Key1', 'Key2'])
print(df_merge_inner)
print()

# merger outer
df_merge_outer = pd.merge(df_left, df_right, how="outer", on=['Key1', 'Key2'])
print(df_merge_outer)
print()

# merger left
df_merge_left = pd.merge(df_left, df_right, how="left", on=['Key1', 'Key2'])
print(df_merge_left)
print()

# merger right
df_merge_right = pd.merge(df_left, df_right, how="right", on=['Key1', 'Key2'])
print(df_merge_right)
print()


# join dataFrames, columns differents

df_left = pd.DataFrame({ 
                         'A' : ['A0', 'A1', 'A2', 'A3'],
                         'B' : ['B0', 'B1', 'B2', 'B3']
                       }, index=[0, 1, 2, 3])

df_right = pd.DataFrame({                         
                          'C' : ['C0', 'C1', 'C2', 'C3'],
                          'D' : ['D0', 'D1', 'D2', 'D3']
                       }, index=[0, 2, 3, 4])

# join only indexs of df_left
df_join = df_left.join(df_right)
print(df_join)
print()

# same all indexs
df_join_outer = df_left.join(df_right, how='outer')
print(df_join_outer)
print()

# 


