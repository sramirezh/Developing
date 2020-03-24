#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:32:58 2019
Study of the theoretical predictions for a gaussian polymer chain 
@author: simon
"""
from __future__ import division
import numpy as np
from scipy.linalg import norm

class polymer(object):
    


    def __init__(self,n_monomers,b):
        self.n_monomers=n_monomers
        self.b=b
        self.generate_polymer()
        self.cm=np.average(self.pos,axis=0)
        self.pos_cm=self.pos-self.cm #Positions shifted by the cm
        self.end_to_end()
        
    def generate_polymer(self):
        """
        Generates a gaussian chain in a 3D lattice
        Args:
        n_monomers the number of monomers
        b the lattice size
        Returns:
        positions an array with all the monomer positions
        """
        n_monomers=self.n_monomers
        b=self.b
        old_position=np.zeros(3)
        positions=[]
        for i in xrange(n_monomers):
            positions.append(old_position)
            x=np.random.randint(0,6)
            displacement=np.zeros(6)
            displacement[x]=1
            disp=np.array([(displacement[0]-displacement[1])*b,(displacement[2]-displacement[3])*b,(displacement[4]-displacement[5])*b])
            new_position=disp+old_position
            old_position=new_position
            
        self.pos=np.array(positions)

        
    def end_to_end(self):
        """
        Args:
            pos is a matrix with all the positions of the monomers
        Returns:
            e2e is the end to end distance of the polymer
        """
        pos=self.pos
        e2e=((pos[-1,0]-pos[0,0])**2+(pos[-1,1]-pos[0,1])**2+(pos[-1,2]-pos[0,2])**2)**0.5
        
        self.e2e=e2e
        


            
        
        


    

def prob_density(n_monomers,b=1):
    """
    Generates the probability density of the end-to-end distance of a gaussian chain
    """
    rmax=n_monomers*b #This can be improved 
    r=np.linspace(0,rmax,100)  
    dist=(2*np.pi*n_monomers*b**2/3)**(-3/2)*np.exp(-3*r**2/(2*n_monomers*b**2))
    
    
    return np.column_stack((r,dist))
    

def gyration_radius(pos):
    """
    Computes the gyration radius, assuming all the particles have the same mass=1
    Args:
        Pos, vector with the positions meassured from the center of mass
    Returns: The scalar gyration radious
    """
    gr2=np.sum(np.average(np.square(pos),axis=0))


    return np.sqrt(gr2)

"""
MAIN
"""


e2e_array=[]
for i in xrange(10000):
    pol=polymer(30,1)
    e2e_array.append(pol.e2e)