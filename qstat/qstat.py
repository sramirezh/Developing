#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:08:10 2018

@author: simon
"""

import pandas as pd
from lxml import etree
import numpy as np
from subprocess import Popen,PIPE

p=Popen(["ls","-h"],stdout=PIPE)

print p.communicate()
data = "out"

tree = etree.parse(data)

lstKey = []
lstValue = []
for p in tree.iter() :
    lstKey.append(tree.getpath(p).replace("/",".")[1:])
    lstValue.append(p.text)
    
df = pd.DataFrame({'key' : lstKey, 'value' : lstValue})
df.sort_values('key')


names=lstKey[1::]
values=lstValue[1::]

parameter_names=[]
for n in names:
    string=n.split('.',2)[-1]
    if 'Job[' in string: #To not include this patter
        continue
    parameter_names.append(string)
    
parameter_names=list(set(parameter_names)) #Deleting the repeated occurrences

"""
'find my jobs"
"""









    


