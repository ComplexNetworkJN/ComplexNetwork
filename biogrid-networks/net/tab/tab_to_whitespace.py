nets=["AT","CE","DM","HS","MM","RN","SC","SP"]
for each in nets:
    f=open(f"{each}.tab","r")
    f2=open(f"{each}.txt","w")

    for line in f:
        p1,p2=line.rstrip().split("\t")
        f2.write(f"{p1} {p2}\n")


    f.close()
    f2.close()
