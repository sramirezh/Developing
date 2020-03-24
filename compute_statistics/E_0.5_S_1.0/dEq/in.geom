# geometry
variable lBulk equal 5.0

variable lhalf equal lz/2.0

variable area equal lx*ly
variable bulk_volume equal ${area}*2.0*${lBulk}
variable total_volume equal ${area}*lz
print "x_length $(lx)" file geometry_info.dat
print "y_length $(ly)" append geometry_info.dat
print "z_length $(lz)" append geometry_info.dat
print "area ${area}" append geometry_info.dat
print "bulk_volume ${bulk_volume}" append geometry_info.dat
print "total_volume ${total_volume}" append geometry_info.dat


variable lB1 equal ${lBulk}
variable lB2 equal lz-${lBulk}

region rBulkB block INF INF INF INF INF ${lB1} units box
region rBulkT block INF INF INF INF ${lB2} INF units box
region rBulk union 2 rBulkB rBulkT


group gSolv type 1 
group gSolu type 2

group gSol union gSolu gSolv
group gPoly type 3
variable nPoly equal count(gPoly)
variable nE1 equal 1
variable nE2 equal ${nPoly}
group gE1 id ${nE1} 
group gE2 id ${nE2}

variable cSolu equal count(gSolu)
variable cSolv equal count(gSolv)
variable cBSolu equal count(gSolu,rBulk)
variable cBSolv equal count(gSolv,rBulk)
variable cBSol equal count(gSol,rBulk)
variable cRatio equal v_cBSolu/v_cBSolv

variable conc_bulk equal v_cBSolu/v_bulk_volume
variable frac_bulk equal v_cBSolu/v_cBSol
#variable cSol equal count(gSol)
variable forc1 equal -v_forc0*v_cRatio
#fix adf0 gSol addforce v_forc0 0.0 0.0
#variable forc1 equal -v_forc0*v_cSolu_bulk/v_cSolv_bulk
variable Ftotal equal v_cSolu*v_forc0+v_cSolv*v_forc1
variable FBulk equal v_cBSolu*v_forc0+v_cBSolv*v_forc1
