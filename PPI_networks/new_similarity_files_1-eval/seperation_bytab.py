X=["ca",'co','do','gu','sh',"ra","rt","pi","mo","ho","hu"]

s=set()
for x in X:
    for y in X:
        if x!=y:
            s.add("-".join(sorted([x,y])))

for each in sorted(s):
    f=open(each+".txt","r")
    f2=open(each+".sim","w")
    for line in f:
        a,b,c = line.rstrip().split(" ")
        f2.write(f"{a}\t{b}\t{c}\n")
    f.close()
    f2.close()
