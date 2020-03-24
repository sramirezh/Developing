#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:16:17 2019
Widom insertion method using pylammps
@author: sr802
"""


from __future__ import division
import numpy as np



from lammps import IPyLammps

import pandas as pd
import argparse
import os
import sys
import time
import random



random.seed(444)

def getting_properties(file_name):
    """
    Returns the intial energy of the system and the box size
    """
    box=[]
    L=IPyLammps()
    L.command("read_data %s"%file_name) #Not necessary to create a new type of particles
    L.pair_style("lj/cut", 3.0)
    L.pair_coeff(1, 1, 1.0, 1.0)
    L.command("pair_modify     tail no")
    L.command("mass * 1.0")
    box.append(L.system.xlo)
    box.append(L.system.xhi)
    box.append(L.system.ylo)
    box.append(L.system.yhi)
    box.append(L.system.zlo)
    box.append(L.system.zhi)
    L.run(0)
    ene_ini=L.eval('pe')
    #This has to be per species
    natoms=L.atoms.natoms
    L.__del__()
    
    return ene_ini,box,natoms

def random_position(box):
    """
    Returns a random position inside the box
    """
    x=random.random()*(box[1]-box[0])+box[0]
    y=random.random()*(box[3]-box[2])+box[0]
    z=random.random()*(box[5]-box[4])+box[0]
    
    return x,y,z


# =============================================================================
# Main
# =============================================================================

t=time.time()

file_name="final_conf_-2.0.dat"
ene_i,box,natoms=getting_properties(file_name)
temperature=2.0
beta=1/temperature
vol=(box[1]-box[0])*(box[3]-box[2])*(box[5]-box[4])
rho=natoms/vol    #Has to be per species

mu_id=temperature*np.log(rho)

n_trials=100
delta_energy=np.zeros(n_trials)



for i in xrange(n_trials):
    L=IPyLammps()
    
    L.atom_style("atomic") #Necessary to create atom maps
    L.command("atom_modify map yes") 
    L.command("read_data %s"%file_name) #Not necessary to create a new type of particles
    L.pair_style("lj/cut", 3.0)
    L.pair_coeff(1, 1, 1.0, 1.0)
    L.command("pair_modify     tail no")
    L.command("mass * 1.0")
    #L.command("include in.interaction")   
    L.create_atoms(1, "single %f %f %f"%(random_position(box)))
    L.run(0)
    ene_f=L.eval('pe')  #Final energy
    delta_energy[i]=ene_f-ene_i
    L.__del__()
    
    
print time.time()-t


boltzmann=np.exp(-beta*delta_energy)
ave_bol=np.average(boltzmann)
mu_ex=-temperature*np.log(ave_bol)
mu=mu_ex+mu_id
#Try to paralellize
#[x for x in dir(L.atoms[0]) if not x.startswith('__')] this tells me the properties of the atoms