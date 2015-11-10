#!/bin/bash

INPUT="ERS"
#INPUT="WPT"
#INPUT="SHP"

VARS=61
#VARS=53
#VARS=329


added=2
suffix=combconfigs.$added

TCL=190
#TCL=114
#TCL=634
CL=$(($TCL + $added))

rm $INPUT.$suffix
rm a.out

#for i in `seq ${VARS}`; do
#    echo "p cnf $VARS $CL" > a.out
#    tail -n +2 $INPUT.dimacs >> a.out
#    echo $i 0 >> a.out
#    pos=`./sharpSAT -q a.out`

#    echo "p cnf $VARS $CL" > a.out
#    tail -n +2 $INPUT.dimacs >> a.out
#    echo -$i 0 >> a.out
#    neg=`./sharpSAT -q a.out`
#    echo $i $pos $neg >> $INPUT.configs
    

#done
for i in `seq $((${VARS}-1))`; do
    for j in `seq $(($i+1)) $((${VARS}))`; do
	#for k in `seq $(($j+1)) $((${VARS}))`; do
	#    echo $i $j $k
	#done
	echo "p cnf $VARS $CL" > a.out
	tail -n +2 $INPUT.dimacs >> a.out
	echo $i 0 >> a.out
	echo $j 0 >> a.out
	pp=`./sharpSAT -q a.out`

	echo "p cnf $VARS $CL" > a.out
	tail -n +2 $INPUT.dimacs >> a.out
	echo $i 0 >> a.out
	echo -$j 0 >> a.out
	pn=`./sharpSAT -q a.out`
	
	echo "p cnf $VARS $CL" > a.out
	tail -n +2 $INPUT.dimacs >> a.out
	echo -$i 0 >> a.out
	echo $j 0 >> a.out
	np=`./sharpSAT -q a.out`
	
	echo "p cnf $VARS $CL" > a.out
	tail -n +2 $INPUT.dimacs >> a.out
	echo -$i 0 >> a.out
	echo -$j 0 >> a.out
	nn=`./sharpSAT -q a.out`
	

	echo $i $j " pp "  $pp " pn "  $pn " np "  $np " nn " $nn >> $INPUT.$suffix
	
	echo $i $j
    done
done