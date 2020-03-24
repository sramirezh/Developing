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
import time
# 3d Lennard-Jones melt


t=time.times()
L = IPyLammps() #Creates the object
L.units("lj")
L.atom_style("full")

L.lattice("fcc", 0.8442)
L.region("box block", 0, 4, 0, 4, 0, 4)
L.create_box(1, "box")
L.create_atoms(1, "box")
L.mass(1, 1.0)

L.command("read_dump config900.dat 900  x y z ix iy iz vx vy vz ")

L.pair_style("lj/cut", 2.5)
L.command("pair_coeff 1 1  1.0  1.0  2.5")
#L.pair_coeff(1, 1, 1.0, 1.0, 2.5)
#L.pair_coeff(1, 1, 1.0, 1.0, 2.5)
#L.pair_coeff(1, 1, 1.0, 1.0, 2.5)

L.command("compute gr all rdf 100 1 1 ")
L.fix(" 2 all ave/time 1 1 1 c_gr[*] file gr.dat mode vector")

L.run(0)


Data=pd.read_csv("gr.dat",sep=" ",skiprows=4,dtype=np.float64,header=None).values

plt.plot(Data[:,1],Data[:,2],label="lammps")
plt.legend()
plt.show()

L.run(0)

print time.time()-t
