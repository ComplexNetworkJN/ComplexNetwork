import pickle

_species=['cat', 'cow', 'dog', 'guinea_pig', 'horse', 'human', 'mouse', 'pig', 'rabbit', 'rta', 'sheep']

PairWise_Set=set()

for each in _species:
    if each!=_species[-1]:
        for i in _species:
            if i!=each:
                PairWise_Set.add(tuple(sorted([each,i])))

#l=["cat","cow","dog","guinea_pig","horse","rabbit","rta","pig","mouse","sheep"]
#11 species
#10 because human has already been done


for each in sorted(PairWise_Set):
    a,b=each
    
    species1_dict=open(f"{a}_dict","rb") #open species dictionary and read bytes
    species2_dict=open(f"{b}_dict","rb") #open species dictionary and read bytes

    
    dspecies1=pickle.load(species1_dict)#loading dictionary
    dspecies2=pickle.load(species2_dict)#loading dictionary
    
    f1= open(f"{a}-{b}","r") #open species file (self-relationship)

    f2=open(f"{a[0:2]}-{b[0:2]}.sim","w")# "\t"   write to sim file
    f3=open(f"{a[0:2]}-{b[0:2]}.txt","w")# " "    write to txt file

    for line in f1:
    #    print(line)i
        #print(line.rstrip().split(' '))
        p1,p2, a,b,c, bit_score, e_val = line.rstrip().split(' ')
        if p1 in dspecies1 and p2 in dspecies2:
            f2.write(f"{dspecies1[p1]}\t{dspecies2[p2]}\t{bit_score}\n")
            f3.write(f"{dspecies1[p1]} {dspecies2[p2]} {bit_score}\n")
    
    # close all files
    species1_dict.close()
    species2_dict.close()
    f1.close()
    f2.close()
    f3.close()
