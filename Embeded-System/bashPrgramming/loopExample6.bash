#!/bin/bash
total=0
number=1

while :
do
    if [ $number -gt 100 ]
    then
        break
    fi
    total=$(( $total + $number ))
    number=$(( $number + 1 ))
done

echo $total