#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 17:37:13 2018
s
@author: sr802
"""



import os
import re
import glob
import numpy as np


s=0#Initial step
d=10000 #Interval
n=100000#FinalTimestep
dmin=0 #Samples to be discarded from vdata.dat


cwd = os.getcwd() #current working directory
dir_path = os.path.dirname(os.path.realpath(__file__))#Path of this python script

#onlyfiles = [f for f in os.listdir(cwd) if os.isfile(os.join(cwd, f))]

numbers=[]
os.chdir(cwd)
directories=glob.glob('E_*')
f=open("Statistics_summary.dat",'w')
for d in directories:
    f.write( "############################################################################")
    
numbers=np.sort(np.array(numbers,dtype=float).reshape((len(numbers))))

f.close()
