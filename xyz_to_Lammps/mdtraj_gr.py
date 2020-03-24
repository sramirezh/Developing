#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 13:03:28 2019

@author: simon
"""

import matplotlib.pyplot as plt
import mdtraj as md

t = md.load_xyz('within.xyz', top='within.xyz')
md.compute_rdf("within.xyz")