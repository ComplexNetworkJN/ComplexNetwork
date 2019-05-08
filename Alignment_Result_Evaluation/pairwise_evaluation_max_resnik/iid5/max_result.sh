#!/bin/bash
Max=/home/sana/Jurisica/IID/Max-orthologs_table.uni.txt


s1=cow;s2=dog;
echo ${s1}_${s2}
awk '{print $8,$13}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $13 != "NA" {print $8,$13}' $Max | wc -l

s1=cow;s2=human;
echo ${s1}_${s2}
awk '{print $8,$1}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $1 != "NA" {print $8,$1}' $Max | wc -l

s1=cow;s2=mouse;
echo ${s1}_${s2}
awk '{print $8,$3}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $3 != "NA" {print $8,$3}' $Max | wc -l

s1=cow;s2=rat;
echo ${s1}_${s2}
awk '{print $8,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $2 != "NA" {print $8,$2}' $Max | wc -l

s1=dog;s2=human;
echo ${s1}_${s2}
awk '{print $13,$1}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$13 != "NA" && $1 != "NA" {print $13,$1}' $Max | wc -l

s1=dog;s2=mouse;
echo ${s1}_${s2}
awk '{print $13,$3}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$13 != "NA" && $3 != "NA" {print $13,$3}' $Max | wc -l

s1=dog;s2=rat;
echo ${s1}_${s2}
awk '{print $13,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$13 != "NA" && $2 != "NA" {print $13,$2}' $Max | wc -l

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



