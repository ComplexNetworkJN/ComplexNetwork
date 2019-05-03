X=["ca",'co','do','gu','sh',"ra","rt","pi","mo","ho","hu"]

s=set()
for x in X:
    for y in X:
        if x!=y:
            s.add("-".join(sorted([x,y])))
print(s)
for a in sorted(s):
    print("awk '{print $1,$2,0}' " + a+".sim > ./iid11_ss=0/"+a+".txt")
