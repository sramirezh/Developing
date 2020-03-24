'''
This scripts determines the viscosity from pressure driven simulations
The only input is the AAVerages.dat

'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev,splrep,splint


# =============================================================================
# input parameters 
# =============================================================================



A=np.loadtxt("AAverages.dat")

# =============================================================================
# Filtering the data from the given ranges
# =============================================================================

'''Getting xmin, i.e after the wall'''
DataInput=A
zpos=1
vpos=3
IndexXmin=np.min(np.where(DataInput[:,vpos]>0)[0]) #Where velocity is different from zero.
xmin=DataInput[IndexXmin,1]
xmax=12

#def DataFilter(xmin,xmax,xpos,DataInput):
#    '''
#    Filters given data depending on the given a parameter in xpos, from xmin to xmax
#    
#    '''


n,m=np.shape(DataInput)
Data=[]
for i in xrange(n):
    if (DataInput[i,zpos]> xmin and DataInput[i,zpos]<xmax ):
        Data.append(DataInput[i,:])

Data=np.array(Data)

        
    

Coeff=np.polyfit(Data[:,zpos],Data[:,vpos],2)
print("\n Need to set the pressure gradient explicitly\n")
PGrad=-0.0005

z=np.linspace(np.min(DataInput[:,1]),np.max(DataInput[:,1]),500)
z=np.linspace(-50,100,500)
vx=np.polyval(Coeff,z)

plt.plot(vx,z)
plt.plot(Data[:,3],Data[:,1],'.')

Viscosity=PGrad/(2*Coeff[0])

print Viscosity
