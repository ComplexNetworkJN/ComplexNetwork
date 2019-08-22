import pickle
L=["AThaliana","CElegans","DMelanogaster","HSapiens","MMusculus"]
L+=["RNorvegicus","SCerevisiae","SPombe"]
for species in L:
    try:
        f=open(f"{species}-3.5.174.el","r")
        f2=open(f"{species[0:2]}.net","w")#output
        f3=open(f"{species[0:2]}_dict","wb")
        i=1
        d=dict()
        for line in f:
            p1,p2=line.rstrip().rsplit("\t")
            if p1 not in d:
                d[p1]=species[0:2]+str(i)
                i+=1
            if p2 not in d:
                d[p2]=species[0:2]+str(i)
                i+=1
            f2.write(f"{d[p1]}\t{d[p2]}\n")
        pickle.dump(d,f3)
    finally:
        f.close()
        f2.close()
        f3.close()

