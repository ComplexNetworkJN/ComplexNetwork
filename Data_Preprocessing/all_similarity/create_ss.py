import pickle

_species=['cat', 'cow', 'dog', 'guinea_pig', 'horse', 'human', 'mouse', 'pig', 'rabbit', 'rat', 'sheep']

PairWise_Set=set()

for each in _species:
    if each!=_species[-1]:
        for i in _species:
            if i!=each:
                PairWise_Set.add(tuple(sorted([each,i])))

#How scripts below are written automatically:
#
#for index,i in enumerate(_species):
#    print(f'f{index+1}=open("{i}_dict_reverse","rb")')
#    print(f'{i}=pickle.load(f{index+1})')
#    print(f'f{index+1}.close()')

f1=open("cat_dict_reverse","rb")
cat=pickle.load(f1)
f1.close()
f2=open("cow_dict_reverse","rb")
cow=pickle.load(f2)
f2.close()
f3=open("dog_dict_reverse","rb")
dog=pickle.load(f3)
f3.close()
f4=open("guinea_pig_dict_reverse","rb")
guinea_pig=pickle.load(f4)
f4.close()
f5=open("horse_dict_reverse","rb")
horse=pickle.load(f5)
f5.close()
f6=open("human_dict_reverse","rb")
human=pickle.load(f6)
f6.close()
f7=open("mouse_dict_reverse","rb")
mouse=pickle.load(f7)
f7.close()
f8=open("pig_dict_reverse","rb")
pig=pickle.load(f8)
f8.close()
f9=open("rabbit_dict_reverse","rb")
rabbit=pickle.load(f9)
f9.close()
f10=open("rat_dict_reverse","rb")
rat=pickle.load(f10)
f10.close()
f11=open("sheep_dict_reverse","rb")
sheep=pickle.load(f11)
f11.close()




for each in PairWise_Set:
    f=open(f"{'-'.join(each)}.sim","w")
    sp1,sp2=each
    i=0
    
    for x in eval(sp1):
        for y in eval(sp2):
            f.write(f"{x}\t{y}\t1\n")
            
#            i+=1
#            if i ==10:
#                break
#        break


    f.close()
