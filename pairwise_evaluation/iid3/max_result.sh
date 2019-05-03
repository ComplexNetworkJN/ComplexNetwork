#!/bin/bash
Max=/home/sana/Jurisica/IID/Max-orthologs_table.uni.txt



s1=human;s2=mouse;
echo ${s1}_${s2}
awk '{print $1,$3}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$1 != "NA" && $3 != "NA" {print $1,$3}' $Max | wc -l

s1=human;s2=rat;
echo ${s1}_${s2}
awk '{print $1,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$1 != "NA" && $2 != "NA" {print $1,$2}' $Max | wc -l

s1=mouse;s2=rat;
echo ${s1}_${s2}
awk '{print $3,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$3 != "NA" && $2 != "NA" {print $3,$2}' $Max | wc -l



