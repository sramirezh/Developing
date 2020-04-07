#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:55:36 2020

@author: simon
"""

def timeConversion(s):
    #
    # Write your code here.
    #
    hour = int(s[:2])
    if s[-2] == 'P':
        return ('%02d%s'%(hour+(hour%12)/hour*12,s[2:-2]))
    else:
        return ('%02d%s'%(int(hour%12),s[2:-2]))