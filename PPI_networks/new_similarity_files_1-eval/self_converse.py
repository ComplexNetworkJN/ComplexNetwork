import pickle

#----
def eval_cal(e:str):
    if "e" in e:
        ind=e.index("e")
        num= eval(e[:ind])*pow(10,(-1)*eval(e[ind+2:].lstrip('0')))
        return 1-num
    else:
        x=1-eval(e)
        return x if x>0 else 0
#----


l=["cat","cow","dog","guinea_pig","human","horse","rabbit","rta","pig","mouse","sheep"]
#11 species


for species in l:
    species_dict=open(f"{species}_dict","rb") #open species dictionary and read bytes

    dspecies=pickle.load(species_dict)#loading dictionary

    f1= open(f"{species}-{species}","r") #open species file (self-relationship)

    f2=open(f"{species}-{species}.sim","w")# "\t"   write to sim file
    f3=open(f"{species}-{species}.txt","w")# " "    write to txt file

    for line in f:
    #    print(line)i
        #print(line.rstrip().split(' '))
        p1,p2, a,b,c, bit_score, e_val = line.rstrip().split(' ')
        if p1 in dspecies and p2 in dspecies:
            f2.write(f"{dspecies[p1]}\t{dspecies[p2]}\t{eval_cal(e_val)}\n")
            f3.write(f"{dspecies[p1]} {dspecies[p2]} {eval_cal(e_val)}\n")
    
    # close all files
    cat.close()
    f.close()
    f2.close()
    f3.close()
