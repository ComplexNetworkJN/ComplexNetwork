file="max_result_iid3.txt"
f1=open(file)
lines=[line.rstrip().split(" ") for line in f1]
f2=open("formated_"+file,"w")

while lines:
    name,found,total=lines[0][0],lines[1][0],lines[2][0]
    total = str(eval(total)-1) # one line of species' names
    lines=lines[3:]
    f2.write(name + " : "+found+" out of "+total + " - about "+str(100*int(found)/int(total))+"%\n")

f1.close()
f2.close()

