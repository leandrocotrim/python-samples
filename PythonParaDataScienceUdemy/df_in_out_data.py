# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 19:46:00 2018

@author: leandro.cotrim
"""
import os
import pandas as pd
# import numpy as np

# read_csv
df = pd.read_csv('./data/exemplo')
df.head()

df = df + 1
df.head()

# isdir and mkdir
if not os.path.isdir('./data/to'):
    os.mkdir('./data/to')
    
# to_csv
df.to_csv('./data/to/exemplo.csv', sep=';', decimal=',')

# read_excel
df = pd.read_excel('./data/Exemplo_Excel.xlsx', sheet_name='Sheet1')
df.head()

df = df * df
df.head()

# to_excel
df.to_excel('./data/to/exemplo.xlsx', sheet_name='Sheet_1')


# read_html
df = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
df.head()
