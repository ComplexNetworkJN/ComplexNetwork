f=open("resnik_result_script_iid11.txt","w")
X=["cat","cow","dog","guinea_pig","sheep","rabbit","rat","pig","mouse","horse","human"]


s=set()
for x in X:
    for y in X:
        if x!=y:
            s.add("-".join(sorted([x,y])))
print(s)

#s1=cow;s2=dog;
#echo ${s1}_${s2}
#cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print "avg = ", sum/NR}'



for each in sorted(s):
    s1,s2=each.split("-")
    f.write(f"s1={s1};s2={s2}\n")
    f.write("echo ${s1}_${s2}\n")
    f.write("cat result_${s1}_${s2}.txt | awk '{sum+=$4} END {print +" '"avg = "'+", sum/NR}'\n")

    f.write("\n")

f.close()
