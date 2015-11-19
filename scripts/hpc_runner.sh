#! /bin/tcsh

if [ "$#" -ne 3 ]; then
  echo "Illegal number parameters"
  echo "sh hpc_benchmark.sh <outfile> <min_processors> <max_processors>"
  exit 1
fi

bsub -W 6000 -n $3 -o out/$1_$2_$3.out.%J -e err/$1_$2_$3.err.%J sh scripts/runner.sh $1 $2 $3 > log/$1_$2_$3.log