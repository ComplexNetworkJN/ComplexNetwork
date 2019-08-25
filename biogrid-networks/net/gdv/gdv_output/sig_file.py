nets=["AT","CE","DM","HS","MM","RN","SC","SP"]
for species in nets:

    f=open(f"{species}.out")
    fout=open(f"{species}.sigs","w")

    for index,line in enumerate(f):
        x=line.rstrip().split(" ")
        fout.write(f"{species}{str(index+1)}"+"\t"+"\t".join(x)+"\n")



