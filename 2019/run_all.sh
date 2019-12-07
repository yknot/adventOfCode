#!/bin/bash

# format all the files
black *.py


# make sure they all run
for f in *_*.py 
do
    if python $f -eq 0; then
        echo "$f passed"
    else
        echo "$f failed XXXXXXXXXXXXXXXX"
    fi

done