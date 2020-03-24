#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:19:02 2018

@author: simon
"""

import matplotlib.pyplot as plt
import numpy as np


axis_font=24
tick_font=20
legend_font=18


x=np.linspace(2.0,3.0)
y=x**2

fig,ax=plt.subplots()
ax.plot(x,y,"-o")
ax.set_ylabel(r'$\log(R_g)$',fontsize=axis_font)
ax.set_xlabel(r'$\log(N) \epsilon$',fontsize=axis_font)

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["text.usetex"] =True