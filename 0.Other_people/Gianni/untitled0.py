#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:10:25 2019
Reads a data file writen with 
@author: simon
"""

import MDAnalysis as mda

u = mda.Universe('final.data', atom_style='id type x y z')

group = u.select_atoms("type 1") 