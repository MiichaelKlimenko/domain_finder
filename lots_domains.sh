#!/bin/bash

FILE=$1

#Check if the file exists
if [ -f $FILE ]; then
    outfile="$FILE-output.txt";
    touch $outfile;
    while read line; do
        echo "Working on $line"...;
        python3 /home/mk/tools/domain_finder/domain_finder.py --company $line | sort -u >> $outfile;
    done <$FILE
    sort -u $outfile;
    echo "Ready. Check $outfile";
else
    echo "Error: File does not exist"
fi