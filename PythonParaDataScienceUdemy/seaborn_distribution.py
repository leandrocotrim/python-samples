# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:34:08 2018

@author: leandro.cotrim
"""

# from collections import Counter
import seaborn as sns

tips = sns.load_dataset('tips') # gorgeta
tips.info()
tips.head()

# distplot
sns.distplot(tips['total_bill'])

sns.distplot(tips['total_bill'], kde=False)

sns.distplot(tips['total_bill'], kde=False, bins=50)


# joinplot
sns.jointplot(x='total_bill', y='tip', data=tips)

sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')

sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')


# pairplot
sns.pairplot(tips, hue='sex')

sns.pairplot(tips, hue='sex', palette='coolwarm')


# rugplot # base kde
sns.rugplot(tips['total_bill'])


# kde
sns.rugplot(tips['total_bill'])
sns.kdeplot(tips['total_bill'])










