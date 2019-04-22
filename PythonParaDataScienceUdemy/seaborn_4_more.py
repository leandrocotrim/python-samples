# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 23:28:21 2018

@author: leandro.cotrim
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# Create a random dataset
data = pd.DataFrame(np.random.random((10,6)), columns=["Iron Man","Captain America","Black Widow","Thor","Hulk", "Hawkeye"])

print(data)
 
# Plot the heatmap
heatmap_plot = sns.heatmap(data, center=0, cmap='gist_ncar')

plt.show()

# ---------------------------------------------------------------------

from scipy.stats import skewnorm

# Create the data
speed = skewnorm.rvs(4, size=50) 
size = skewnorm.rvs(4, size=50)
 
# Create and shor the 2D Density plot
ax = sns.kdeplot(speed, size, cmap="Reds", shade=False, bw=.15, cbar=True)
ax.set(xlabel='speed', ylabel='size')
plt.show()

# ---------------------------------------------------------------------

arr = [[1,'Iron Man',83,80,75,70,70],
[2,'Captain America',60,62,63,80,80],
[3,'Thor',80,82,83,100,100],
[3,'Hulk',80,100,67,44,92],
[4,'Black Widow',52,43,60,50,65],
[5,'Hawkeye',58,64,58,80,65]]

df = pd.DataFrame(arr, columns=["#", "Name","Attack","Defense","Speed","Range","Health"])

# Get the data for Iron Man
labels=np.array(["Attack","Defense","Speed","Range","Health"])
stats=df.loc[0,labels].values

# Make some calculations for the plot
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles,[angles[0]]))

# Plot stuff
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.set_title([df.loc[0,"Name"]])
ax.grid(True)

plt.show()

# ----------------------------------------------------------------------

from scipy.cluster import hierarchy

# Read in the dataset
# Drop any fields that are strings
# Only get the first 40 because this dataset is big
df = pd.read_csv('.\data\Pokemon.csv')
df = df.set_index('Name')
del df.index.name
df = df.drop(["Type 1", "Type 2", "Legendary"], axis=1)
df = df.head(n=40)
 
# Calculate the distance between each sample
Z = hierarchy.linkage(df, 'ward')
 
# Orientation our tree
hierarchy.dendrogram(Z, orientation="left", labels=df.index)

plt.show()

# ----------------------------------------------------------------------



