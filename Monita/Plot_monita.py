#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:26:14 2019

@author: simon
"""

import matplotlib.pyplot as plt
import numpy as np


opacity = 0.4
bar_width = 0.35
yoffset=0.05

fig,ax = plt.subplots()

label = ['Baja California','Mexico City','Quintana Roo', 'Tamaulipas']
Perc_2008 = [9.3,7.8,10.1,10.3]
Perc_2016 = [13.5,10.3,14.9,10.0]

plt.rcParams['font.family'] = 'verdana'
plt.rcParams['font.serif'] = 'verdana'

index1 = np.arange(len(label))
index2 = index1+bar_width
bar1 = ax.bar(index1, Perc_2008,bar_width, label = '2008',color = "#42b6f5" )
bar2 = ax.bar(index2,Perc_2016,bar_width, label = '2016',color = '#424ef5')
ax.set_xlabel('Bundesstaat', fontsize=15)
ax.set_ylabel('Prozent', fontsize=15)
plt.xticks(index1+0.5*bar_width, label, fontsize=10, rotation=0)
plt.yticks(fontsize=10)
ax.set_title('Drogenkonsum von Menschen im Alter von \n 12-65 Jahren')

# Add counts above the two bar graphs
for rect in bar1 + bar2:
    height = rect.get_height()
    print (height)
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%2.1f' % height, ha='center', va='bottom')



ymin,ymax=ax.get_ylim()
deltay=ymax-ymin


ax.set_ylim(ymin,ymax+deltay*yoffset)

plt.legend()
plt.tight_layout()
plt.savefig("plot_monita.pdf")
plt.savefig("plot_drugs.png", dpi=300)