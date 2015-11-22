#!/usr/bin/env bash

if [ "$#" -ne 4 ]; then
  echo "Illegal number parameters"
  exit 1
fi

for (( N=$3; N<=$4; N++ ))
  do
    echo "\nNumber of processors : $N"
    $PYTHON runner.py $1 $2 $N
done


