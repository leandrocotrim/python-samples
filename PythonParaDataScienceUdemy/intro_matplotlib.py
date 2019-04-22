# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:35:55 2018

@author: leandro.cotrim
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x * x

# functional
plt.plot(x, y, 'r--') # red with ------
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Título')
plt.show()


plt.subplots(nrows=2, ncols=2)
plt.show()


plt.subplot(1, 2, 1) # working with first element
plt.plot(x, y, 'r--')
plt.subplot(1, 2, 2) # working with second element
plt.plot(y, x, 'g*-')
plt.show()


# OOP
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # [left, bottom, width, height] -> posicional
axes1.plot(x, y)
axes1.set_xlabel('X')
axes1.set_ylabel('Y')
axes1.set_title('Title')

axes2 = fig.add_axes([0.2, 0.5, 0.3, 0.3]) # [left, bottom, width, height] -> posicional
axes2.plot(y, x)
axes2.set_xlabel('X')
axes2.set_ylabel('Y')
axes2.set_title('Title')


# multi axes
fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Titulo')

ax.plot(x, x**3, 'b--')
ax.plot(x, x**4, 'g.-')


# multi plots
fig, ax = plt.subplots(2, 2)

for row in ax:
    for item in row:
        item.set_xlabel('x')
        item.set_ylabel('y')
        item.set_title('Titulo')

ax[0,0].plot(y, y**2, 'r--')
ax[0,1].plot(y, x**2, 'g*-')
ax[1,0].plot(x, x**2, 'y.-')
ax[1,1].plot(x, y**y, 'o-')
plt.tight_layout()


# figure dimension
fig2, ax2 = plt.subplots(figsize=(4,4)) # length all print
ax2.plot(x, y)

# build image
fig.savefig('plots.jpg')

from PIL import Image
with Image.open('plots.jpg') as img:
    img.show()


# legend

fig, ax = plt.subplots()
ax.plot(x, y, label="Vendas")
ax.plot(y, x, label="Compra")
ax.legend() # optional loc= 1, 2, 3, 4


# ----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import lines
from matplotlib.lines import Line2D

x = np.linspace(0, 5, 11)
y = x * x

plt.plot(x, y, color='red', ls='-.', label='Spacing', alpha=0.5, lw=2)
plt.plot(y, x, color='blue', ls=':', label='Spacing X')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('With out OOP')
plt.legend()

# --------------------------------------------------------------

lineStyles = [k for k in lines.lineStyles.keys() if k not in ['None', ' ','']]

def get_linestyle():
    for ls in lineStyles:
        yield ls

def get_color():
    for c in ['red', 'green', 'blue', 'orange']:
        yield c

g_ls = get_linestyle()
g_c  = get_color()


fig, axs = plt.subplots(2, 2)
for row in axs:    
    for ax in row:        
        color = next(g_c)
        linestyle = next(g_ls)
        label = color + ' : ' + linestyle
        ax.plot(x, y, color=color, linestyle=linestyle, label=label)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('With OOP')
        ax.legend()
        
plt.tight_layout()

# ----------------------------------------------------------------------------

fn = lambda k: k != None and ((type(k) is int) or (len(k) == 1 and k != ' '))
markers = [k for k in Line2D.markers if fn(k)]

def get_markers():
    for m in markers:
        yield m
        
g_m = get_markers()

x = np.linspace(0,5,5)
y = x * x

fig, axs = plt.subplots(37, 1, figsize=(10, 40))
for ax in axs:    
    marker = next(g_m)
    label = marker + ' str' if marker is str else str(marker) + ' int'        
    ax.plot(x, y, label=label, linestyle='None', marker=marker)
    ax.set_xlabel = 'X'
    ax.set_ylabel = 'Y'
    ax.set_title('With markers')

plt.tight_layout()

# ----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(x, y, color='orange', ls='-.', alpha=0.8, lw=3)
ax.plot(y, x, color='yellow', ls='None', marker='o', alpha=1, lw=1)

# shop chart
ax.set_xlim([2, 10])
ax.set_ylim([2, 8])





























    




