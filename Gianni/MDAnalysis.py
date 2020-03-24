#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:10:25 2019
Reads a data file writen with Lammps, writen in LJ units, distances are measured in particle diameters \simga

@author: simon
"""

import MDAnalysis as mda
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist,squareform


def convert_into_real(length,characteristic,dim):
    """
    Converts into microns
    Args:
        lenght: coulde be an array or single number, in length, area, volume
        characteristic is the normalisation factor
        dim 1 if length, 3 if volume
    """
    scaling = characteristic
    length = length * (scaling)**dim
    
    return length


u = mda.Universe('final.data', atom_style='id type x y z')

geometry = u.coord  #

atoms = u.select_atoms("type 1") 

positions = atoms.positions #It organises the atoms


real_radius = 150 *10**-3 #Radius in microns

pos_m = squareform(pdist(positions))

np.fill_diagonal(pos_m,100)

# =============================================================================
# Basic checks in real units
# =============================================================================

print ("\nThe minimum distance between spheres is %s" %np.min(pos_m))


vol_atom = 4/3 *np.pi*(0.5)**3
ff = atoms.n_atoms* vol_atom / geometry.volume

print ("The old ff is %lf" %ff)

# =============================================================================
# Pair correlation
# =============================================================================
from MDAnalysis.analysis.rdf import InterRDF

rdf = InterRDF(atoms,atoms,exclusion_block = (1,1),range = [0,2.5],verbose = True)
rdf.run()

plt.plot(rdf.bins, rdf.rdf)
plt.savefig("gr.pdf")
plt.show()



# =============================================================================
# Converting to real units
# =============================================================================

diameter = 2*real_radius

positions = convert_into_real(positions,diameter,1)

np.savetxt("real_positions.txt",positions)


pos_m = squareform(pdist(positions))
np.fill_diagonal(pos_m,100)

print ("The box side is (IF IT IS FCC) %f"%convert_into_real(geometry.volume**(1/3),diameter,1))
print ("\nThe minimum distance between spheres is %s" %np.min(pos_m))

new_ff =  atoms.n_atoms* convert_into_real(vol_atom,diameter,3) / convert_into_real(geometry.volume,diameter,3)

print ("The new ff is %lf" %new_ff)






