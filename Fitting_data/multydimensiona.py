#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:10:12 2019

@author: simon
"""
import numpy as np
from pylab import *
from scipy import *






#Lets create the known polynomial

def p_known(x,y):
    z=3*x*y**2+4*y*x**2+5*x**2
    return z


n_points=40

x=np.linspace(0,10)
y=np.linspace(0,10)
z=p_known(x,y)

zerr= 0.2 * z                      # simulated errors (10%)