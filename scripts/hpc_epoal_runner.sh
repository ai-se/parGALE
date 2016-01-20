#! /bin/tcsh

if [ "$#" -ne 4 ]; then
  echo "Illegal number parameters"
  echo "sh scripts/hpc_epoal_runner.sh <model> <outfile> <min_processors> <max_processors>"
  exit 1
fi

bsub -W 6000 -n 16 -o out/$2_$3_$4.out.%J -e err/$2_$3_$4.err.%J sh scripts/epoal_runner.sh $1 $2 $3 $4 > log/$2_$3_$4.log