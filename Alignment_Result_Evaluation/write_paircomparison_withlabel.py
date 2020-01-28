import pickle

def add_tofile(protein1,protein2,specie1,specie2):
    file="-".join(sorted([specie1,specie2])) #   "a-b"
    try:
        file=open(f"{file}.txt","a+")
        file.write(f"{protein1} {protein2}\n")
    finally:
        file.close()

def write_file(spe_pro_dict): # {specie : [protein] , s : [p]}
    a=tuple(spe_pro_dict.keys())
    s=set()
    for each in a:
        if each!=a[-1]:

            for i in a:
                if i!=each:
                    s.add(tuple(sorted([each,i])))
    
    for (a,b) in s:
        if spe_pro_dict[a]!=[] and spe_pro_dict[b]!=[]:
            add_tofile(spe_pro_dict[a][0],spe_pro_dict[b][0],a,b)






try:
 
    
    f5=open("5iid_sim_CIQ_15000_5000_5000.txt","r")       # r - cleaning this file
    



    p=[]

    p2=[]
    for line in f5:
        try:
            human,mouse,rat,cow,dog = line.rstrip().split("\t")
    
            x={"human":[],"rat":[],"mouse":[],"cow":[],"dog":[]}
        
            
            if "-" not in human:
                x["human"].append(human)
            
            if "-" not in rat:
                x["rat"].append(rat)

            if "-" not in mouse:
                x["mouse"].append(mouse)

            if "-" not in cow:
                x["cow"].append(cow)

            if "-" not in dog:
                x["dog"].append(dog)
        
            write_file(x)
        except Exception as ex:
            print(ex)
            print(uniq)
            print(line)
            break



    print(len(p))
    print(p)



finally:

    f5.close()

