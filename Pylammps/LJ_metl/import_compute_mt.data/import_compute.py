#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 23:38:24 2018
Trying to import a configuration and compute something, in this case just computing g(r)
@author: simon
"""

import pandas as pd
import numpy as np
from lammps import IPyLammps
import matplotlib.pyplot as plt
# 3d Lennard-Jones melt

L = IPyLammps() #Creates the object
L.units("lj")
L.atom_style("full")


L.command("read_data mt.data")

L.pair_style("lj/cut", 2.5)
L.command("pair_coeff * *  1.0  1.0  2.5")
#L.pair_coeff(1, 1, 1.0, 1.0, 2.5)
#L.pair_coeff(1, 1, 1.0, 1.0, 2.5)
#L.pair_coeff(1, 1, 1.0, 1.0, 2.5)

L.command("compute gr all rdf 100 1 1 ")
L.fix(" 2 all ave/time 1 1 1 c_gr[*] file gr.dat mode vector")

L.run(0)

