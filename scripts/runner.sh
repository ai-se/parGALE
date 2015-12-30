#!/usr/bin/env bash

if [ "$#" -ne 5 ]; then
  echo "Illegal number parameters"
  exit 1
fi

for (( N=$5; N<=$6; N++ ))
  do
    echo "\nNumber of processors : $N"
    $PYTHON runner.py $1 $2 $3 $N $4
done


