#!/bin/sh
DirCur=`pwd`
CMD_SLAB='/frenkelscratch/sr802/DiffusioP/programs/poly'
CMD_MT='/home/sr802/Programs/mylammps/tools/moltemplate/moltemplate/scripts/moltemplate.sh'
SCT_AWK='../mt.awk'
ELL=1
HEIGHT=30
LX=20
LY=20
if [ $# -eq 1 ]
  then
    LY=$1
fi
LZ=30
PN=30
if [ $# -eq 2 ]
  then
    PN=1
fi
PL=2.0
SOLF=0.1
DW=1.1
CH=1
#Number of Water Molecules
NWATER=100000
#Number of Directroy
NOD=10

#for i in `seq 1 $NOD`
#do
S=`expr $i + 1395`
#if [ $i -ge 10 ]
#then
# cd 'd'$i
#else
# cd 'd0'$i
#fi

#cd dSetBox
echo "SEED is "$S > seed.txt
$CMD_SLAB -lx $LX -ly $LY -lz $LZ -a $SOLF -ch $CH -lw $DW -se $S -pn $PN -pl $PL > mt.c
cp ../mtt.lt ./
awk -v NWT=$NWATER -f $SCT_AWK mtt.lt mt.c > mt.lt
echo "moltemplate processing..."
$CMD_MT mt.lt 
echo "moltemplate finished"
cd ..
cd ..
#done
