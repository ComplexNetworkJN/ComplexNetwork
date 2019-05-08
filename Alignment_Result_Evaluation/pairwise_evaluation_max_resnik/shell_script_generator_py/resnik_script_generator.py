f=open("resnik_script_iid11.txt","w")
X=["cat","cow","dog","guinea_pig","sheep","rabbit","rat","pig","mouse","horse","human"]


s=set()
for x in X:
    for y in X:
        if x!=y:
            s.add("-".join(sorted([x,y])))
print(s)

#   /home/sana/bin/resnik -a cow-dog.align > ./result_cow_dog.txt

address = "/home/sana/bin/resnik"
flag= "-a"

for each in sorted(s):

    f.write(f"{address} {flag} {each}.align > ./result_{each}.txt\n")
#    f.write("\n")

f.close()
