#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:26:14 2019

@author: simon
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd





df = pd.read_csv("statistics.csv", skiprows = 1, header = None, usecols=[0,1], decimal=',' )
df.columns = ['year','homicides']
df.astype('int32').dtypes

df['homicides'] = 1000 * df['homicides']

data = df.values

opacity = 0.4
bar_width = 0.35
yoffset=0.05

fig,ax = plt.subplots()
#style.use('fivethirtyeight')
plt.rcParams['font.family'] = 'verdana'
plt.rcParams['font.serif'] = 'verdana'
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False

#ax.tick_params(axis = 'both', which = 'minor', labelsize = 18)
ax.plot(data[:,0],data[:,1],'o-', c ='b')

#ax.set_xlabel('Jahr', fontsize = 20)
#ax.set_ylabel('Morde', fontsize = 20)
plt.yticks(fontsize = 10)
plt.xticks(np.arange(1990,2020,4),fontsize = 10)


ax.set_title('Mordrate in Mexiko (1990-2018)', fontsize = 15)





ymin,ymax=ax.get_ylim()
deltay=ymax-ymin


ax.set_ylim(ymin,ymax+deltay*yoffset)


plt.tight_layout()
plt.savefig("plot_homicides.pdf")
plt.savefig("plot_homicides.png", dpi=300)