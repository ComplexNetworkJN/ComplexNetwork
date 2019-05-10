import pickle

l=["cat","cow","dog","guinea_pig","horse","rabbit","rat","pig","mouse","sheep"]
#11 species
#10 because human has already been done


for species in l:
    species_dict=open(f"{species}_dict","rb") #open species dictionary and read bytes

    dspecies=pickle.load(species_dict)#loading dictionary

    f1= open(f"{species}-{species}","r") #open species file (self-relationship)

    f2=open(f"{species}-{species}.sim","w")# "\t"   write to sim file
    f3=open(f"{species}-{species}.txt","w")# " "    write to txt file

    for line in f1:
    #    print(line)i
        #print(line.rstrip().split(' '))
        p1,p2, a,b,c, bit_score, evalue = line.rstrip().split(' ')
        if p1 in dspecies and p2 in dspecies:
            f2.write(f"{dspecies[p1]}\t{dspecies[p2]}\t{bit_score}\n")
            f3.write(f"{dspecies[p1]} {dspecies[p2]} {bit_score}\n")
    
    # close all files
    species_dict.close()
    f1.close()
    f2.close()
    f3.close()
