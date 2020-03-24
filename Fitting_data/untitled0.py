#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:53:18 2019
Analysing the multifitting 
using 
https://scipy.github.io/old-wiki/pages/Cookbook/FittingData.html#Fitting_a_power-law_to_data_with_errors
@author: simon
"""

from pylab import *
from scipy import *

# Define function for calculating a power law
powerlaw = lambda x, amp, index: amp * (x**index)

##########
# Generate data points with noise
##########
num_points = 20

# Note: all positive, non-zero data
xdata = linspace(1.1, 10.1, num_points) 
ydata = powerlaw(xdata, 10.0, -2.0)     # simulated perfect data
yerr = 0.2 * ydata                      # simulated errors (10%)

ydata += randn(num_points) * yerr       # simulated noisy data



##########
# Fitting the data -- Least Squares Method
##########

# Power-law fitting is best done by first converting
# to a linear equation and then fitting to a straight line.
#
#  y = a * x^b
#  log(y) = log(a) + b*log(x)
#

logx = log10(xdata)
logy = log10(ydata)
logyerr = yerr / ydata

# define our (line) fitting function
fitfunc = lambda p, x: p[0] * x + p[1]   
errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err

pinit = [-1.0, 1.0]
out = optimize.leastsq(errfunc, pinit,
                       args=(logx, logy, logyerr), full_output=1)

pfinal = out[0]
covar = out[1]
print pfinal
print covar

index = pfinal[0]
amp = 10.0**pfinal[1]

indexErr = sqrt( covar[0][0] ) 
ampErr = sqrt( covar[1][1] ) * amp

##########
# Plotting data
##########

clf()
subplot(2, 1, 1)
plot(xdata, powerlaw(xdata, amp, index))     # Fit
errorbar(xdata, ydata, yerr=yerr, fmt='k.')  # Data
text(5, 6.5, 'Ampli = %5.2f +/- %5.2f' % (amp, ampErr))
text(5, 5.5, 'Index = %5.2f +/- %5.2f' % (index, indexErr))
title('Best Fit Power Law')
xlabel('X')
ylabel('Y')
xlim(1, 11)

subplot(2, 1, 2)
loglog(xdata, powerlaw(xdata, amp, index))
errorbar(xdata, ydata, yerr=yerr, fmt='k.')  # Data
xlabel('X (log scale)')
ylabel('Y (log scale)')
xlim(1.0, 11)

savefig('power_law_fit.png')


#Trying to fit with numpy

import numpy as np

p_numpy=np.polyfit(logx,logy,w=1/logyerr,deg=1, cov=True)

pfinal_np=p_numpy[0]
covar_np=p_numpy[1]

print pfinal_np
print covar_np