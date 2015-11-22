#! /bin/tcsh

if [ "$#" -ne 4 ]; then
  echo "Illegal number parameters"
  echo "sh hpc_benchmark.sh <model> <outfile> <min_processors> <max_processors>"
  exit 1
fi

bsub -W 6000 -n $4 -o out/$2_$3_$4.out.%J -e err/$2_$3_$4.err.%J sh scripts/runner.sh $1 $2 $3 $4 > log/$2_$3_$4.log