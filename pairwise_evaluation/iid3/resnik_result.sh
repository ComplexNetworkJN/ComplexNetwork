#!/bin/bash


s1=human;s2=mouse;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'

s1=human;s2=rat;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'

s1=mouse;s2=rat;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'
