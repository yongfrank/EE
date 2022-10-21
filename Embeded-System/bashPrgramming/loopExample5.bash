#!/bin/bash
total=0
for number in `seq 1 1 100`
do
    total=$(( $total + $number ))
done

echo $total
