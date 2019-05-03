f=open("max_script_iid5.txt","w")
#X=["cat",'cow','dog','guinea_pig','sheep',"rabbit","rat","pig","mouse","horse"]
X=['human','cow','rat','dog','mouse']


d={'cat': 12,'cow': 8,'dog': 13,'guinea_pig': 14, 'sheep': 11, 'rabbit': 15, 'rat': 2, 'pig': 10, 'mouse': 3, 'horse': 9,'human':1}
s=set()




for x in X:
    for y in X:
        if x!=y:
            s.add("-".join(sorted([x,y])))



print(s)
for each in sorted(s):
    sp1,sp2=each.split("-")
    f.write(f"s1={sp1};s2={sp2};\n")
    f.write("echo ${"+"s1"+"}_${"+"s2"+"}\n")
    f.write("awk '{print $"+str(d[sp1])+",$"+str(d[sp2])+"}' $Max | fgrep -f - ${"+"s1"+"}-${"+"s2"+"}.align | wc -l\n")
    f.write("awk '$"+str(d[sp1])+" != "+'"NA" && $'+str(d[sp2])+" != "+'"NA" {print $'+str(d[sp1])+",$"+str(d[sp2])+"}' $Max | wc -l\n")
    f.write("\n")
    
f.close()
