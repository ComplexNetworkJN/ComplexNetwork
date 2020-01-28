import pickle
L=["cat","pig","cow","rabbit","rat","human"]
L+=["sheep","guinea_pig","mouse","dog","horse"]


one_reverse_dict_iid=dict()
for each in L:
    
    try:
        
        f1=open(f"{each}_dict","rb")  # input
#        f2=open(f"{each}_dict_reverse","wb")#node set

        b=pickle.load(f1)
        
        
        for each in b.keys():
            one_reverse_dict_iid[b[each]]=each


    finally:
        f1.close()


ff=open("one_reverse_dict_iid","wb")
pickle.dump(one_reverse_dict_iid,ff)
ff.close()
