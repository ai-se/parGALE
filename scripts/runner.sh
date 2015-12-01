#!/usr/bin/env bash

if [ "$#" -ne 5 ]; then
  echo "Illegal number parameters"
  exit 1
fi

for (( N=$4; N<=$5; N++ ))
  do
    echo "\nNumber of processors : $N"
    $PYTHON runner.py $1 $2 $3 $N
done


