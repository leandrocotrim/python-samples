# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:27:21 2018

@author: leandro.cotrim
"""

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

# read Css
df = pd.read_csv('.\data\911.csv')

# print info
df.info()

# print head
df.head(5)

# top 5 zips
df['zip'].value_counts().head(5)

# top 5 twp
df['twp'].value_counts().head(5)

# count unique titles
df['title'].nunique()

# new column and apply
f_type_title = lambda title: title.split(':')[0] 
df['reason'] = df['title'].apply(f_type_title)

# reason more common
df['reason'].value_counts()

# plot count with reason
sns.countplot(data=df, x='reason')

# what's type columns timestamp
type(df['timeStamp'].iloc[0])

# cast string timestamp to datetime
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# new type
type(df['timeStamp'].iloc[0])

# create new columns hour, month, day of week
df['hour'] = df['timeStamp'].apply(lambda t: t.hour)
df['month'] = df['timeStamp'].apply(lambda t: t.month)

dmap = { 0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun' }
df['dayofweek'] = df['timeStamp'].apply(lambda t: dmap[t.dayofweek])

# plot count base day of week
sns.countplot(data=df,x='dayofweek')

# plot count base day of week segregation reason 
sns.countplot(data=df,x='dayofweek',hue='reason')

# plot count base month segregation reason 
sns.countplot(data=df,x='month',hue='reason')

# group byMonth
byMonth = df.groupby('month')

# aggregation count
aggCount = byMonth.count()

# head
aggCount.head()

# plot count for month
aggCount['e'].plot()

# create column with indexs
aggCount.reset_index(inplace=True)
sns.lmplot(data=aggCount, x='month', y='e')

# Create column date
df['date'] = df['timeStamp'].apply(lambda t: t.date())

# groub by date
gDate = df.groupby('date')
aggCount = gDate.count()

# plot count
aggCount['e'].plot()

# plot count reason 1
df[df['reason']=='EMS'].groupby('date').count()['twp'].plot()

# plot count reason 2
df[df['reason']=='Fire'].groupby('date').count()['twp'].plot()

# plot count reason 3
df[df['reason']=='Traffic'].groupby('date').count()['twp'].plot()

#---

# Pivot index = dayofweek columns = hour 
df_w_h = df[['dayofweek','hour','e']].groupby(['dayofweek','hour']).count()
df_w_h = df_w_h['e'].unstack()

# heatmap
sns.heatmap(data=df_w_h)

# clustermap
sns.clustermap(data=df_w_h)

#---

# Pivot index = dayofweek columns = month
df_dm = df[['dayofweek','month','e']].groupby(['dayofweek','month']).count()
df_dm = df_dm['e'].unstack()

# heatmap
sns.heatmap(df_dm)

# clustemap
sns.clustermap(df_dm)
