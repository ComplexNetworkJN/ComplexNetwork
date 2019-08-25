
max_gdv=0
for each in ["AT","CE","DM","HS","MM","RN","SC","SP"]:
    f=open(f"{each}.sigs","r")
    for line in f:
        p_name,*values=line.rstrip().split("\t")
        for v in values:
            max_gdv=max(max_gdv,int(v))

    
    
    f.close()
print(f"Largest Value is {max_gdv}")
