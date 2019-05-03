#!/bin/bash

s1=cow;s2=dog;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'

s1=cow;s2=human;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'

s1=cow;s2=mouse;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'

s1=cow;s2=rat;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'

s1=dog;s2=human;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'

s1=dog;s2=mouse;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'

s1=dog;s2=rat;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'

s1=human;s2=mouse;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'

s1=human;s2=rat;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'

s1=mouse;s2=rat;
echo ${s1}_${s2}
cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'
