#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:40:58 2020

This is a covariance test
@author: simon
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
from statsmodels.tsa.stattools import acf

n = 1000000
a = np.random.rand(n)

import time 

t = time.time()
acf(a)

print (time.time()-t)
cov1 = np.cov(a,a)



#half_n = np.floor(n/2)
#tau_array = np.arange(0, half_n, dtype = int)
#
#correlation = []
#error = []
#
## by hand
#for tau in tau_array:
#    
#    if tau == 0:
#        x = a*a
#    else:
#        x = a[:-tau]*np.roll(a,-tau)[:-tau]
#        
#    correlation.append(np.sum(x)/len(x))
#    error.append(sem(x)) # Assuming they are independent
#    
#correlation_2 = []
## With covariance
#for tau in tau_array:
#    
#    if tau == 0:
#        x = np.cov(a,a)[0][1]
#    else:
#        x = np.cov(a[:-tau],np.roll(a,-tau)[:-tau])[0][1]
#        
#    correlation_2.append(x)
#
#correlation_2 = correlation_2/correlation_2[0]
#
#
#
#
#
#    
#correlation = correlation/correlation[0]
#
#correlation_3 = acf(a,nlags = 3)
#    




def autocorrelation_error (A):
    """
    Computes an autocorrelation analysis
    Args:
        A matrix with the data in columns of a matrix A[n,m]
    Returns:
        C Correlation of the data 
        corrTime Correlation time of the data.
    """
    n,m=np.shape(A)
    C=np.zeros((n,m)) #Autocorrelation
    corrTime=np.zeros(m)
    for k in range(m):
        vector = A[:,k]
        i=0;
        tol=0.0001
        val=10
        sign=True
        while val>tol and sign == True:
            if i == 0:
                C[i,k] = np.cov(vector,vector)[0][1]
            else:
                C[i,k] = np.cov(vector[:-i],np.roll(vector,-i)[:-i])[0][1]
            val = C[i,k]
            if i>0:
                sign = C[i,k]<C[i-1,k]
                corrTime[k] = corrTime[k]+C[i,k]/C[0,k]
            i+= 1
    corrTime  = 0.5 + corrTime
    return C, corrTime