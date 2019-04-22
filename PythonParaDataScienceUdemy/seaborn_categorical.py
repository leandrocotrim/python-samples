# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:34:08 2018

@author: leandro.cotrim
"""

import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')
tips.info()
tips.head()


# barplot
sns.barplot(x='sex', y='total_bill', data=tips)

sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)


# countplot
sns.countplot(y='sex', data=tips)


# boxplot
sns.boxplot(x='day', y='total_bill', data=tips)

sns.boxplot(x='day', y='total_bill', data=tips, palette='rainbow')

sns.boxplot(x='day', y='total_bill', data=tips, palette='rainbow', hue='sex')

sns.boxplot(data=tips, palette='rainbow', orient='h')


# violinplot
sns.violinplot(x='day', y='total_bill', data=tips)

sns.violinplot(x='day', y='total_bill', data=tips, hue='sex')

sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)


# stripplot
sns.stripplot(x='day', y='total_bill', data=tips)

sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)

sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex')

sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', split=True)


# swarmplot
sns.swarmplot(x='day', y='total_bill', data=tips)

sns.swarmplot(x='day', y='total_bill', data=tips, hue='sex')

sns.swarmplot(x='day', y='total_bill', data=tips, hue='sex', split=True)

sns.swarmplot(x='day', y='total_bill', data=tips, color='black')
sns.violinplot(x='day', y='total_bill', data=tips)

# factorplot
sns.factorplot(x='day', y='total_bill', data=tips, kind='bar')

sns.factorplot(x='day', y='total_bill', data=tips, kind='violin')

sns.factorplot(x='day', y='total_bill', data=tips, kind='swarm')

sns.factorplot(x='day', y='total_bill', data=tips, kind='strip')

sns.factorplot(x='day', y='total_bill', data=tips, kind='box')

sns.factorplot(x='day', data=tips, kind='count')
