import pickle
species_dict=open("cat_dict","rb") #open species dictionary and read bytes


dspecies=pickle.load(cat)


f1= open("cat-cat","r") #open species file (self-relationship)

f2=open("cat-cat.sim","w")# "\t"   write to sim file
f3=open("cat-cat.txt","w")# " "    write to txt file

for line in f:
#    print(line)i
    #print(line.rstrip().split(' '))
    p1,p2, a,b,c, bit_score, evalue = line.rstrip().split(' ')
    if p1 in dspecies and p2 in dspecies:
        f2.write(f"{dspecies[p1]}\t{dspecies[p2]}\t{evalue}\n")
        f3.write(f"{dspecies[p1]} {dspecies[p2]} {evalue}\n")
        
# close all files
cat.close()
f.close()
f2.close()
f3.close()
