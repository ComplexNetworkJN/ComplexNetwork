#!/bin/bash
Max=/home/weishew/research/Max-orthologs_table.uni.txt

s1=cat;s2=cow;
echo ${s1}_${s2}
awk '{print $12,$8}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$12 != "NA" && $8 != "NA" {print $12,$8}' $Max | wc -l

s1=cat;s2=dog;
echo ${s1}_${s2}
awk '{print $12,$13}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$12 != "NA" && $13 != "NA" {print $12,$13}' $Max | wc -l

s1=cat;s2=guinea_pig;
echo ${s1}_${s2}
awk '{print $12,$14}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$12 != "NA" && $14 != "NA" {print $12,$14}' $Max | wc -l

s1=cat;s2=horse;
echo ${s1}_${s2}
awk '{print $12,$9}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$12 != "NA" && $9 != "NA" {print $12,$9}' $Max | wc -l

s1=cat;s2=human;
echo ${s1}_${s2}
awk '{print $12,$1}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$12 != "NA" && $1 != "NA" {print $12,$1}' $Max | wc -l

s1=cat;s2=mouse;
echo ${s1}_${s2}
awk '{print $12,$3}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$12 != "NA" && $3 != "NA" {print $12,$3}' $Max | wc -l

s1=cat;s2=pig;
echo ${s1}_${s2}
awk '{print $12,$10}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$12 != "NA" && $10 != "NA" {print $12,$10}' $Max | wc -l

s1=cat;s2=rabbit;
echo ${s1}_${s2}
awk '{print $12,$15}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$12 != "NA" && $15 != "NA" {print $12,$15}' $Max | wc -l

s1=cat;s2=rat;
echo ${s1}_${s2}
awk '{print $12,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$12 != "NA" && $2 != "NA" {print $12,$2}' $Max | wc -l

s1=cat;s2=sheep;
echo ${s1}_${s2}
awk '{print $12,$11}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$12 != "NA" && $11 != "NA" {print $12,$11}' $Max | wc -l

s1=cow;s2=dog;
echo ${s1}_${s2}
awk '{print $8,$13}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $13 != "NA" {print $8,$13}' $Max | wc -l

s1=cow;s2=guinea_pig;
echo ${s1}_${s2}
awk '{print $8,$14}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $14 != "NA" {print $8,$14}' $Max | wc -l

s1=cow;s2=horse;
echo ${s1}_${s2}
awk '{print $8,$9}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $9 != "NA" {print $8,$9}' $Max | wc -l

s1=cow;s2=human;
echo ${s1}_${s2}
awk '{print $8,$1}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $1 != "NA" {print $8,$1}' $Max | wc -l

s1=cow;s2=mouse;
echo ${s1}_${s2}
awk '{print $8,$3}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $3 != "NA" {print $8,$3}' $Max | wc -l

s1=cow;s2=pig;
echo ${s1}_${s2}
awk '{print $8,$10}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $10 != "NA" {print $8,$10}' $Max | wc -l

s1=cow;s2=rabbit;
echo ${s1}_${s2}
awk '{print $8,$15}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $15 != "NA" {print $8,$15}' $Max | wc -l

s1=cow;s2=rat;
echo ${s1}_${s2}
awk '{print $8,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $2 != "NA" {print $8,$2}' $Max | wc -l

s1=cow;s2=sheep;
echo ${s1}_${s2}
awk '{print $8,$11}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$8 != "NA" && $11 != "NA" {print $8,$11}' $Max | wc -l

s1=dog;s2=guinea_pig;
echo ${s1}_${s2}
awk '{print $13,$14}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$13 != "NA" && $14 != "NA" {print $13,$14}' $Max | wc -l

s1=dog;s2=horse;
echo ${s1}_${s2}
awk '{print $13,$9}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$13 != "NA" && $9 != "NA" {print $13,$9}' $Max | wc -l

s1=dog;s2=human;
echo ${s1}_${s2}
awk '{print $13,$1}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$13 != "NA" && $1 != "NA" {print $13,$1}' $Max | wc -l

s1=dog;s2=mouse;
echo ${s1}_${s2}
awk '{print $13,$3}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$13 != "NA" && $3 != "NA" {print $13,$3}' $Max | wc -l

s1=dog;s2=pig;
echo ${s1}_${s2}
awk '{print $13,$10}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$13 != "NA" && $10 != "NA" {print $13,$10}' $Max | wc -l

s1=dog;s2=rabbit;
echo ${s1}_${s2}
awk '{print $13,$15}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$13 != "NA" && $15 != "NA" {print $13,$15}' $Max | wc -l

s1=dog;s2=rat;
echo ${s1}_${s2}
awk '{print $13,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$13 != "NA" && $2 != "NA" {print $13,$2}' $Max | wc -l

s1=dog;s2=sheep;
echo ${s1}_${s2}
awk '{print $13,$11}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$13 != "NA" && $11 != "NA" {print $13,$11}' $Max | wc -l

s1=guinea_pig;s2=horse;
echo ${s1}_${s2}
awk '{print $14,$9}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$14 != "NA" && $9 != "NA" {print $14,$9}' $Max | wc -l

s1=guinea_pig;s2=human;
echo ${s1}_${s2}
awk '{print $14,$1}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$14 != "NA" && $1 != "NA" {print $14,$1}' $Max | wc -l

s1=guinea_pig;s2=mouse;
echo ${s1}_${s2}
awk '{print $14,$3}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$14 != "NA" && $3 != "NA" {print $14,$3}' $Max | wc -l

s1=guinea_pig;s2=pig;
echo ${s1}_${s2}
awk '{print $14,$10}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$14 != "NA" && $10 != "NA" {print $14,$10}' $Max | wc -l

s1=guinea_pig;s2=rabbit;
echo ${s1}_${s2}
awk '{print $14,$15}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$14 != "NA" && $15 != "NA" {print $14,$15}' $Max | wc -l

s1=guinea_pig;s2=rat;
echo ${s1}_${s2}
awk '{print $14,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$14 != "NA" && $2 != "NA" {print $14,$2}' $Max | wc -l

s1=guinea_pig;s2=sheep;
echo ${s1}_${s2}
awk '{print $14,$11}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$14 != "NA" && $11 != "NA" {print $14,$11}' $Max | wc -l

s1=horse;s2=human;
echo ${s1}_${s2}
awk '{print $9,$1}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$9 != "NA" && $1 != "NA" {print $9,$1}' $Max | wc -l

s1=horse;s2=mouse;
echo ${s1}_${s2}
awk '{print $9,$3}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$9 != "NA" && $3 != "NA" {print $9,$3}' $Max | wc -l

s1=horse;s2=pig;
echo ${s1}_${s2}
awk '{print $9,$10}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$9 != "NA" && $10 != "NA" {print $9,$10}' $Max | wc -l

s1=horse;s2=rabbit;
echo ${s1}_${s2}
awk '{print $9,$15}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$9 != "NA" && $15 != "NA" {print $9,$15}' $Max | wc -l

s1=horse;s2=rat;
echo ${s1}_${s2}
awk '{print $9,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$9 != "NA" && $2 != "NA" {print $9,$2}' $Max | wc -l

s1=horse;s2=sheep;
echo ${s1}_${s2}
awk '{print $9,$11}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$9 != "NA" && $11 != "NA" {print $9,$11}' $Max | wc -l

s1=human;s2=mouse;
echo ${s1}_${s2}
awk '{print $1,$3}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$1 != "NA" && $3 != "NA" {print $1,$3}' $Max | wc -l

s1=human;s2=pig;
echo ${s1}_${s2}
awk '{print $1,$10}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$1 != "NA" && $10 != "NA" {print $1,$10}' $Max | wc -l

s1=human;s2=rabbit;
echo ${s1}_${s2}
awk '{print $1,$15}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$1 != "NA" && $15 != "NA" {print $1,$15}' $Max | wc -l

s1=human;s2=rat;
echo ${s1}_${s2}
awk '{print $1,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$1 != "NA" && $2 != "NA" {print $1,$2}' $Max | wc -l

s1=human;s2=sheep;
echo ${s1}_${s2}
awk '{print $1,$11}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$1 != "NA" && $11 != "NA" {print $1,$11}' $Max | wc -l

s1=mouse;s2=pig;
echo ${s1}_${s2}
awk '{print $3,$10}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$3 != "NA" && $10 != "NA" {print $3,$10}' $Max | wc -l

s1=mouse;s2=rabbit;
echo ${s1}_${s2}
awk '{print $3,$15}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$3 != "NA" && $15 != "NA" {print $3,$15}' $Max | wc -l

s1=mouse;s2=rat;
echo ${s1}_${s2}
awk '{print $3,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$3 != "NA" && $2 != "NA" {print $3,$2}' $Max | wc -l

s1=mouse;s2=sheep;
echo ${s1}_${s2}
awk '{print $3,$11}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$3 != "NA" && $11 != "NA" {print $3,$11}' $Max | wc -l

s1=pig;s2=rabbit;
echo ${s1}_${s2}
awk '{print $10,$15}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$10 != "NA" && $15 != "NA" {print $10,$15}' $Max | wc -l

s1=pig;s2=rat;
echo ${s1}_${s2}
awk '{print $10,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$10 != "NA" && $2 != "NA" {print $10,$2}' $Max | wc -l

s1=pig;s2=sheep;
echo ${s1}_${s2}
awk '{print $10,$11}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$10 != "NA" && $11 != "NA" {print $10,$11}' $Max | wc -l

s1=rabbit;s2=rat;
echo ${s1}_${s2}
awk '{print $15,$2}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$15 != "NA" && $2 != "NA" {print $15,$2}' $Max | wc -l

s1=rabbit;s2=sheep;
echo ${s1}_${s2}
awk '{print $15,$11}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$15 != "NA" && $11 != "NA" {print $15,$11}' $Max | wc -l

s1=rat;s2=sheep;
echo ${s1}_${s2}
awk '{print $2,$11}' $Max | fgrep -f - ${s1}-${s2}.align | wc -l
awk '$2 != "NA" && $11 != "NA" {print $2,$11}' $Max | wc -l

