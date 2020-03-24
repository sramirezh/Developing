#This script has the geometry and group definitions

#####################################################
#Group definitions
#####################################################
group 	gSolv type 1
group	gSolu type 2
group	gWall type 3

group 	gFluid union gSolv gSolu


region 	rBulk block  INF INF INF INF 10 25

#Diffusive layer

#"All" system but far from reflective wall

region rSystem block INF INF INF INF 0 25

