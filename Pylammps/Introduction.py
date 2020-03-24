#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 18:16:59 2018
This is usefull to perform the widom calculation
@author: simon
"""

from lammps import PyLammps

from lammps import IPyLammps
L = PyLammps()
Li =IPyLammps
L.file("in.melt") #Reads and runs a lammps script

Li.file("in.melt")
#print("Potential energy: ", L.eval("pe"))


#L.region("box block", 0, 10, 0, 5, -0.5, 0.5)
#L.write_script("input.lmp") #Writes the session to another file
