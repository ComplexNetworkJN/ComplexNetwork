file="resnik_script_iid11.txt"
f1=open(file)




#   /home/sana/bin/resnik -a cow-dog.align > ./result_cow_dog.txt

while lines:
    name,found,total=lines[0][0],lines[1][0],lines[2][0]
    lines=lines[3:]
    f2.write(name + " : "+found+" out of "+total + " - about "+str(100*int(found)/int(total))+"%\n")

f1.close()
f2.close()

