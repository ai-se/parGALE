#!/bin/bash

topdir=`pwd`
for exp in ERS #WPT #ERS WPT SHP
do
    cd $exp
    expdir=`pwd`
    for cores in 2 4 8 16 32 64 
    do
	depth=`perl -l -e "print log($cores)/log(2)"`
	cd $expdir
	cd $cores
	coresdir=`pwd`
	for i in `seq 1 10` 
	do
	    cd $coresdir
	    cd r$i
	    rundir=`pwd`
	    cd $topdir
	    echo $exp
            echo $rundir
	    python MapDimacsBackToBestVars.py $exp ${rundir}/dimacsvars ${rundir}/bestvars
	    
	done
    done
done
