import math
def fo(file_name):
    fo_dict={}
    file=open(file_name,'r')
    for lines in file.readlines():
        line=lines.rstrip().split('\t')
        if len(line)>1:
            fo_dict[line[0]]=line[1:]
    return fo_dict
A_fo=fo('./CG/A.fo')
B_fo=fo('./CG/B.fo')
C_fo=fo('./CG/C.fo')
D_fo=fo('./CG/D.fo')
E_fo=fo('./CG/E.fo')
F_fo=fo('./CG/F.fo')
G_fo=fo('./CG/G.fo')
H_fo=fo('./CG/H.fo')
def fo_map(data):
    if (data[0]).upper() == 'A':
        fo_dic = A_fo
    elif (data[0]).upper() == 'B':
        fo_dic = B_fo
    elif (data[0]).upper() == 'C':
        fo_dic = C_fo
    elif (data[0]).upper() == 'D':
        fo_dic = D_fo
    elif (data[0]).upper() == 'E':
        fo_dic = E_fo
    elif (data[0]).upper() == 'F':
        fo_dic = F_fo
    elif (data[0]).upper() == 'G':
        fo_dic = G_fo
    elif (data[0]).upper() == 'H':
        fo_dic = H_fo
    return fo_dic
f=open('clusters.txt','r')
annotated_cluster=[]
cluster_number=0
consistent=0
for lines in f.readlines():
    line=lines.rstrip().split(' ')
    count=0
    for data in line:
        fo_dic=fo_map(data)
        if data in fo_dic.keys():
            count=count+1
        if count==2:
            break
    if count == 2:
        annotated_cluster.append(line)
        cluster_number=cluster_number+1
f.seek(0)
def NE(C_list):
    C_dict={}
    new_C_dict={}
    C_truple=[]
    for i in C_list:
        if i in fo_map(i).keys():
            C_dict[i]=fo_map(i)[i]
            for j in fo_map(i)[i]:
                C_truple.append((j,i))
    for a in C_truple:
        if new_C_dict.__contains__(a[0]):
            new_C_dict[a[0]].append(a[1])
        else:
            new_C_dict[a[0]] = [a[1]]
    d=len(new_C_dict)
    sum_pi=0
    p_denominator = []
    p_i=[]
    if d==1:
        ne=0
    else:
        for i in new_C_dict.values():
            p_denominator.append(len(i))
        denominator=sum(p_denominator)
        for j in p_denominator:
            pi=j/denominator
            p_i.append(pi)
        for a in p_i:
            sum_pi=sum_pi+a*math.log(a)
        ne=-sum_pi/math.log(d)
    return ne


MNE_list=[]
for i in range(cluster_number):
    cluster_i=annotated_cluster[i]
    MNE_list.append(NE(cluster_i))
#print(MNE_list)
MNE=sum(MNE_list)/len(MNE_list)
print(MNE)
