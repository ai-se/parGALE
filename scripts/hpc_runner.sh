#! /bin/tcsh

if [ "$#" -ne 5 ]; then
  echo "Illegal number parameters"
  echo "sh hpc_benchmark.sh <model> <outfile> <min_processors> <max_processors>"
  exit 1
fi

bsub -W 2500 -n 20 -o out/$3_$4_$5.out.%J -e err/$3_$4_$5.err.%J sh scripts/runner.sh $1 $2 $3 $4 $5 > log/$3_$4_$5.log
