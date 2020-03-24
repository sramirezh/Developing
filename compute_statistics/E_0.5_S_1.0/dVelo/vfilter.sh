#!/bin/bash

INIT=4

INPUT_FILE_NAME=prof2d_vel.dat
OUTPUT_FILE_NAME=vel2d.dat

     cat ${INPUT_FILE_NAME} | awk '
        BEGIN{
                print "variables=x y rho vx vr"
                print "zone i=40, j=20"; 
        }
        {
                if(FNR>4) {
	 		if ($2=='9.75') {
				$6=0.0;
				$7=0.0;
				}
            		print $3, $2, $5, $6, $7;
                        }
        }
	' > ${OUTPUT_FILE_NAME}

INPUT_FILE_NAME=prof2d_con.dat
OUTPUT_FILE_NAME=con2d.dat

     cat ${INPUT_FILE_NAME} | awk '
        BEGIN{
                print "variables=x y c"
                print "zone i=40, j=20"; 
        }
        {
                if(FNR>4) {
	 		if ($2=='9.75') {
				$5=0.068;
				}
            		print $3, $2, $5;
                        }
        }
	' > ${OUTPUT_FILE_NAME}

