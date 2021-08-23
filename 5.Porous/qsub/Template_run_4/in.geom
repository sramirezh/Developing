#This script has the geometry and group definitions

####################################################
# geometry
####################################################


variable lhalfx equal lx/2.0
variable lhalfy equal ly/2.0
variable lhalfz equal lz/2.0

variable area equal lx*ly
print "x_length $(lx)" file geometry_info.dat
print "y_length $(ly)" append geometry_info.dat
print "z_length $(lz)" append geometry_info.dat
print "area ${area}" append geometry_info.dat

#####################################################
#Groups definitions
#####################################################
group gSolv type 1 
group gSolu type 2
group gMon type 3
group gSol union gSolu gSolv
