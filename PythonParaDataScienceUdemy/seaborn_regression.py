# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 00:16:14 2018

@author: leandro.cotrim
"""

import numpy as np
import seaborn as sns

tips = sns.load_dataset('tips')
tips.info()
tips.head()

# linear model == lm

sns.lmplot(x='total_bill', y='tip', data=tips)

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex')

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', col='smoker')

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', col='smoker', row='day')

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', col='smoker')
