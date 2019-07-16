
f1=open("rt.tab","r")#human mouse rat
file=iter(f1)
next(file)

f=open("rt.in","w")

s=''
num_line=0
num_node=set()
for line in file:
    p1,p2=line.rstrip().split("\t")
    num_line+=1
    p1=str(int(p1[2:])-1)
    p2=str(int(p2[2:])-1)
    num_node.add(p1)
    num_node.add(p2)
    s+=f'{p1} {p2}\n'
    
    
    


f.write(f"{str(len(num_node))} {str(num_line)}\n"+s)
