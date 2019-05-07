#Note:
#This py file is used to check if
#   there are equal number of keys
#   and values for each dictionary
#   to ensure we don't make some
#   silly bugs.


import pickle
f=open("rabbit_dict_reverse","rb")
#f=open("test_iid5_human","rb")
d=pickle.load(f)
f.close()
#print(d['ca1450']==d['ca1451'])
print(len(d.keys()),"key")
print(len(set(d.values())),"values")
i=0
for each in d.keys():
    if "ra" not in each:
        i+=1
print(i)

print(type(d.keys()))
