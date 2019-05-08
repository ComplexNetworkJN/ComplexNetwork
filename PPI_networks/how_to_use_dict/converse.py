import pickle
cat=open("cat_dict","rb")
cow=open("cow_dict","rb")

dcat=pickle.load(cat)
dcow=pickle.load(cow)

f= open("cat-cow","r")

f2=open("cat-cow.sim","w")# "\t"
f3=open("cat-cow.txt","w")# " "

for line in f:
#    print(line)i

    print(line.rstrip().split(' '))
    p1,p2, a,b,c, bit_score, evalue = line.rstrip().split(' ')
    f2.write(f"{dcat[p1]}\t{dcow[p2]}\t{evalue}\n")
    f3.write(f"{dcat[p1]} {dcow[p2]} {evalue}\n")

