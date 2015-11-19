#!/usr/bin/env bash

if [ "$#" -ne 3 ]; then
  echo "Illegal number parameters"
  exit 1
fi

for (( N=$2; N<=$3; N++ ))
  do
    echo "\nNumber of processors : $N"
    $PYTHON algorithms/parallel/gale/multi_gale.py $1 $N
done


