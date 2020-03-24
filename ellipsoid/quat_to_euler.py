#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:07:35 2019

@author: simon
"""
import transformations as tf
import numpy as np
name="final_3d.dat"
data=np.loadtxt(name,skiprows=9)


angles = tf.transformations.euler_from_quaternion([-0.315,  0.003,  0.901, -0.300],axes='sxyz')
print angles


