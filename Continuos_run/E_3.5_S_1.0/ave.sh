#!/bin/bash

sl=1003
el=10003

if [ $# -eq 1 ]; then
	sl=$1
elif [ $# -eq 2 ]; then
	sl=$1
	el=$2
fi

cat vdata.dat | awk "NR==$sl,NR==$el{print}" > tmp1.dat
cat tmp1.dat | awk '{print $2}' > tmp2.dat
cat tmp1.dat | awk '{print $7}' > tmp3.dat
cat tmp1.dat | awk '{print $8}' > tmp4.dat
cat tmp1.dat | awk '{print $6}' > tmp5.dat

{
	cat tmp2.dat
} | awk '
	{
		sum += $1
	}
	END{
		printf "velocity %.16e\n", sum / NR
	}
'

{
	cat tmp3.dat
} | awk '
	{
		sum += $1
	}
	END{
		printf "bulk conc %.16e\n", sum / NR
	}
'

{
	cat tmp4.dat
} | awk '
	{
		sum += $1
	}
	END{
		printf "bulk mfrac %.16e\n", sum / NR
	}
'

{
        cat tmp5.dat
} | awk '
        {
                sum += $1
        }
        END{
                printf "Rg2 %.16e\n", sum / NR
        }
'

