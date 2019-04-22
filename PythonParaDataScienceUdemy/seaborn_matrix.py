# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:34:08 2018

@author: leandro.cotrim
"""

import seaborn as sns

tips = sns.load_dataset('tips')
tips.info()
tips.head()
crr = tips.corr()

sns.heatmap(crr)

sns.heatmap(crr, cmap='coolwarm')

sns.heatmap(crr, cmap='coolwarm', annot=True)

# ---------------------------------------------------------------------------

flights = sns.load_dataset('flights')
flights.info()
flights.head()

ptf = flights.pivot_table(values='passengers', index='month', columns='year')

sns.heatmap(ptf)

sns.heatmap(data=ptf, annot=True)

sns.heatmap(ptf, cmap='coolwarm')

sns.heatmap(ptf, cmap='magma')

sns.heatmap(ptf, cmap='magma', linecolor='white', linewidths=1)

sns.heatmap(ptf, cmap='magma', linecolor='gray', linewidths=1)

# --

sns.clustermap(ptf)

sns.clustermap(ptf, standard_scale=1, annot=True)







