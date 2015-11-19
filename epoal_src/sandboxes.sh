#!/bin/bash

topdir=`pwd`
for exp in ERS #WPT SHP
do
    rm -r $exp
    mkdir $exp
    cd $exp
    expdir=`pwd`
    for cores in 2 4 8 16 32 64 
    do
	depth=`perl -l -e "print log($cores)/log(2)"`
	cd $expdir
	mkdir $cores
	cd $cores
	coresdir=`pwd`
	for i in `seq 1 10`
	do
	    cd $coresdir
	    mkdir r$i
	    cd r$i
	    rundir=`pwd`
	    cd $topdir
	    python ConfigCounter.py $exp $depth "${rundir}/"
	    
	done
    done
done
