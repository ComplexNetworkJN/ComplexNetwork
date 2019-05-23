import pickle
Saved=set()
PairWise_Set=set()
_={"cat":[],"cow":[],"dog":[],"guinea_pig":[],"horse":[],"human":[],"mouse":[],"pig":[],"rabbit":[],"rat":[],"sheep":[]}
_t=tuple(_.keys())
for each in _t:
    if each!=_t[-1]:
        for i in _t:
            if i!=each:
                PairWise_Set.add(tuple(sorted([each,i])))



def add_tofile(protein1,protein2,specie1,specie2):
    file="-".join(sorted([specie1,specie2])) #   "a-b"
    try:
        file=open(f"{file}.txt","a+")
        file.write(f"{protein1} {protein2}\n")
    except Exception as ex:
        print(ex)
        print(protein1,protein2,specie1,specie2)
    
    finally:
        file.close()
#        f1.close()
#        f2.close()


def write_file(a_list): # {specie : [protein] , s : [p]} #list now
    spe_pro_dict={"cat":[],"cow":[],"dog":[],"guinea_pig":[],"horse":[],"human":[],"mouse":[],"pig":[],"rabbit":[],"rat":[],"sheep":[]}
    
    for each in a_list:
        if "ca" in each:
            spe_pro_dict["cat"].append(each)
        elif "co" in each:
            spe_pro_dict["cow"].append(each)
        elif "do" in each:
            spe_pro_dict["dog"].append(each)
        elif "gu" in each:
            spe_pro_dict["guinea_pig"].append(each)
        elif "ho" in each:
            spe_pro_dict["horse"].append(each)
        elif "hu" in each:
            spe_pro_dict["human"].append(each)
        elif "mo" in each:
            spe_pro_dict["mouse"].append(each)
        elif "pi" in each:
            spe_pro_dict["pig"].append(each)
        elif "ra" in each:
            spe_pro_dict["rabbit"].append(each)
        elif "rt" in each:
            spe_pro_dict["rat"].append(each)
        elif "sh" in each:
            spe_pro_dict["sheep"].append(each)
                
                
#    a=tuple(spe_pro_dict.keys())
#    s=set()
#    for each in a:
#        if each!=a[-1]:
#            for i in a:
#                if i!=each:
#                    s.add(tuple(sorted([each,i])))


    for (a,b) in PairWise_Set:
        if spe_pro_dict[a]!=[] and spe_pro_dict[b]!=[] and (spe_pro_dict[a][0],spe_pro_dict[b][0]) not in Saved and (spe_pro_dict[b][0],spe_pro_dict[a][0]) not in Saved :
            Saved.add((spe_pro_dict[a][0],spe_pro_dict[b][0]))
            
            add_tofile(spe_pro_dict[a][0],spe_pro_dict[b][0],a,b)






try:

    f=input("input alignment result file name:")
    print("opening: ",f)
    sep=input("is the protein seperated by tab[1] or whitespace[2]: ")
    while int(sep)!=1 and int(sep)!=2:
        print("Wrong command! Try again!")
        sep=input("is the protein seperated by tab[1] or whitespace[2]: ")
    file=open(f,"r")       # r - cleaning this file
    

    p=[]
    p2=[]
    i=0
    for line in file:
       
        try:
            if int(sep)==1:
                nodes = line.rstrip().split("\t")
            elif int(sep)==2:
                nodes = line.rstrip().split(" ")
            spe_pro_dict={"cat":[],"cow":[],"dog":[],"guinea_pig":[],"horse":[],"human":[],"mouse":[],"pig":[],"rabbit":[],"rat":[],"sheep":[]}
    
            for each in nodes:
                if "ca" in each:
                    spe_pro_dict["cat"].append(each)
                elif "co" in each:
                    spe_pro_dict["cow"].append(each)
                elif "do" in each:
                    spe_pro_dict["dog"].append(each)
                elif "gu" in each:
                    spe_pro_dict["guinea_pig"].append(each)
                elif "ho" in each:
                    spe_pro_dict["horse"].append(each)
                elif "hu" in each:
                    spe_pro_dict["human"].append(each)
                elif "mo" in each:
                    spe_pro_dict["mouse"].append(each)
                elif "pi" in each:
                    spe_pro_dict["pig"].append(each)
                elif "ra" in each:
                    spe_pro_dict["rat"].append(each)
                elif "rt" in each:
                    spe_pro_dict["rabbit"].append(each)
                elif "sh" in each:
                    spe_pro_dict["sheep"].append(each)
        
            for i in spe_pro_dict["cat"]:
                for each in nodes:
                    if each not in spe_pro_dict["cat"]:
                        write_file([i,each])
                            
            for i in spe_pro_dict["cow"]:
                for each in nodes:
                    if each not in spe_pro_dict["cat"] and each not in spe_pro_dict["cow"]:
                        write_file([i,each])

            for i in spe_pro_dict["dog"]:
                for each in nodes:
                    if each not in spe_pro_dict["cat"] and each not in spe_pro_dict["cow"] and each not in spe_pro_dict["dog"]:
                        write_file([i,each])
            
            for i in spe_pro_dict["guinea_pig"]:
                for each in nodes:
                    if each not in spe_pro_dict["cat"] and each not in spe_pro_dict["cow"] and each not in spe_pro_dict["dog"] and each not in spe_pro_dict["guinea_pig"]:
                        write_file([i,each])
                            
                            
            for i in spe_pro_dict["horse"]:
                for each in nodes:
                    if each not in spe_pro_dict["cat"] and each not in spe_pro_dict["cow"] and each not in spe_pro_dict["dog"] and each not in spe_pro_dict["guinea_pig"] and each not in spe_pro_dict["horse"]:
                        write_file([i,each])
                            
            for i in spe_pro_dict["human"]:
                for each in nodes:
                    if each not in spe_pro_dict["cat"] and each not in spe_pro_dict["cow"] and each not in spe_pro_dict["dog"] and each not in spe_pro_dict["guinea_pig"] and each not in spe_pro_dict["horse"] and each not in spe_pro_dict["human"]:
                        write_file([i,each])
                            
            for i in spe_pro_dict["mouse"]:
                for each in nodes:
                    if each not in spe_pro_dict["cat"] and each not in spe_pro_dict["cow"] and each not in spe_pro_dict["dog"] and each not in spe_pro_dict["guinea_pig"] and each not in spe_pro_dict["horse"] and each not in spe_pro_dict["human"] and each not in spe_pro_dict["mouse"]:
                        write_file([i,each])

            for i in spe_pro_dict["pig"]:
                for each in nodes:
                    if each not in spe_pro_dict["cat"] and each not in spe_pro_dict["cow"] and each not in spe_pro_dict["dog"] and each not in spe_pro_dict["guinea_pig"] and each not in spe_pro_dict["horse"] and each not in spe_pro_dict["human"] and each not in spe_pro_dict["mouse"] and each not in spe_pro_dict["pig"]:
                        write_file([i,each])

            for i in spe_pro_dict["rat"]:
                for each in nodes:
                    if each not in spe_pro_dict["cat"] and each not in spe_pro_dict["cow"] and each not in spe_pro_dict["dog"] and each not in spe_pro_dict["guinea_pig"] and each not in spe_pro_dict["horse"] and each not in spe_pro_dict["human"] and each not in spe_pro_dict["mouse"] and each not in spe_pro_dict["pig"] and each not in spe_pro_dict["rat"]:
                        write_file([i,each])

            for i in spe_pro_dict["rabbit"]:
                for each in nodes:
                    if each not in spe_pro_dict["cat"] and each not in spe_pro_dict["cow"] and each not in spe_pro_dict["dog"] and each not in spe_pro_dict["guinea_pig"] and each not in spe_pro_dict["horse"] and each not in spe_pro_dict["human"] and each not in spe_pro_dict["mouse"] and each not in spe_pro_dict["pig"] and each not in spe_pro_dict["rat"] and each not in spe_pro_dict["rabbit"]:
                        write_file([i,each])
    
            


            
            
        except Exception as ex:
            print(ex)
         
            print(line)
            break

    print("Finished")



finally:
#    f0.close()
#    f1.close()
#    f2.close()
#    f3.close()
#    f4.close()
    file.close()
