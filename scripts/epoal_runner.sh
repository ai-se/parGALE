#!/usr/bin/env bash

if [ "$#" -ne 4 ]; then
  echo "Illegal number parameters"
  echo "sh scripts/epoal_runner.sh <model> <filename> <min procs> <max procs>"
  exit 1
fi

for (( N=$3; N<=$4; N++ ))
  do
    echo "\nNumber of processors : $N"
    $PYTHON epoal_src/pnpGIA.py $1 $2 $N
done