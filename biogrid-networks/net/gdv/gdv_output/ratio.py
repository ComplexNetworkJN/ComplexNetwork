
#Largest_Value=15457085047084
Largest_Value =6657378763587
Four_Bit=pow(2,4*8)-1
Ratio=Four_Bit/Largest_Value



s=''
for each in ["AT","CE","DM","HS","MM","RN","SC","SP"]:
    temp=''
    f=open(f"{each}.sigs","r")
    f1=open(f"{each}_ratio.sigs","w")
    for line in f:
        p_name,*values=line.rstrip().split("\t")
        temp=f"{p_name}"
        for v in values:
            temp+=f"\t{int(int(v)*Ratio)}"
        
        
        s+=temp+"\n"
    f1.write(s)

    f1.close()
    f.close()
