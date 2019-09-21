import pickle

f=open("one_reverse_dict","rb")
d=pickle.load(f)
file_name=input("Enter File Name:")

_sep=input("Enter [1] if seperated by tab, [2] if by whitespace:")
if _sep=="1":
    sep="\t"
elif _sep=="2":
    sep=" "
else:
    raise Exception("Not the correct number")

input_f=open(file_name)
ff=open("converted_"+file_name,"w")
try:
    for line in input_f:
        nodes=line.rstrip().split(sep)
        cluster=f"{sep}".join(d[i][1:] for i in [_ for _ in nodes if _ in d])
        if len(cluster.split(sep))>1:
            ff.write(cluster+"\n")
    
    print("Done")
except:
    print(line.rstrip().split(sep))
