#This script has the geometry and group definitions

####################################################
# geometry
####################################################

variable lBulk equal 5.0

variable lhalfx equal lx/2.0
variable lhalfy equal ly/2.0
variable lhalfz equal lz/2.0

variable area equal lx*ly
variable bulk_volume equal ${area}*2.0*${lBulk}
variable total_volume equal ${area}*lz
print "x_length $(lx)" file geometry_info.dat
print "y_length $(ly)" append geometry_info.dat
print "z_length $(lz)" append geometry_info.dat
print "area ${area}" append geometry_info.dat
print "bulk_volume ${bulk_volume}" append geometry_info.dat
print "total_volume ${total_volume}" append geometry_info.dat

#####################################################
#Bulk definitions
#####################################################

variable lB1 equal ${lBulk} 
variable lB2 equal lz-${lBulk}

region rBulkB block INF INF INF INF INF ${lB1} units box
region rBulkT block INF INF INF INF ${lB2} INF units box
region rBulk union 2 rBulkB rBulkT

#region rNo_bulk block INF INF INF INF ${lB1} ${lB2} units box

#####################################################
#Groups definitions
#####################################################
group gSolv type 1 

group gSolu type 2
group gPoly type 3
group gSol union gSolu gSolv

variable nPoly equal count(gPoly)
variable nE1 equal 1
variable nE2 equal ${nPoly}
group gE1 id ${nE1} 
group gE2 id ${nE2}
