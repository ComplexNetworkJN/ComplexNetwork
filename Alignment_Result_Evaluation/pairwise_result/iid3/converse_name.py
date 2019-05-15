import pickle

s=set()
l=["human","mouse","rat"]
for x in l:
    for y in l:
        if x!=y:
            s.add("-".join(sorted([x,y])))
L=[each for each in s]


fmouse=open(f"mouse_dict_reverse","rb")
frat=open(f"rat_dict_reverse","rb")
fhuman=open(f"human_dict_reverse","rb")

_human=pickle.load(fhuman)
_mouse=pickle.load(fmouse)
_rat=pickle.load(frat)


fmouse.close()
frat.close()
fhuman.close()


for each in sorted(L):
    sp1,sp2=each.split("-")
    fread =open(each+".txt"  ,"r")
    fwrite=open(each+".align","w")
    SAVED=set()
    for line in fread:
        
        p1,p2=line.rstrip().split(" ")
    
    #rat are renamed rt123, rt124. So we need to first change ra to rt;
    #ps: if in the original input data, rat has already been changed to rt123...
    #then, just comment out the above if statements;
           
        if (eval('_'+sp1)[p1],eval('_'+sp2)[p2]) not in SAVED:
            SAVED.add((eval('_'+sp1)[p1],eval('_'+sp2)[p2]))
            fwrite.write(f"{eval('_'+sp1)[p1]} {eval('_'+sp2)[p2]}\n")
        else:
            print(p1,p2,sp1,sp2)
            print(eval('_'+sp1)[p1],eval('_'+sp2)[p2])
            print((eval('_'+sp1)[p1],eval('_'+sp2)[p2])  in SAVED)
            print("broken")
            #print what you need here if there are bugs:-(
            break
    
    fread.close()
    fwrite.close()


