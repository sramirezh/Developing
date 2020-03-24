#!/bin/bash

sl=103
el=10003

if [ $# -eq 1 ]; then
	sl = $1
elif [ $# -eq 2 ]; then
	sl = $1
	el = $2
fi

cat vdata.dat | awk "NR==$sl,NR==$el{print}" > tmp1.dat
cat tmp1.dat | awk '{print $2}' > tmp2.dat

{
	cat tmp2.dat
} | awk '
	{
		sum += $1
	}
	END{
		printf "%.16e\n", sum / NR
	}
'

