from collections import Counter
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
print('annotated_cluster',cluster_number)
f.seek(0)
for i in range(cluster_number):
    cluster_i=annotated_cluster[i]
    length=len(cluster_i)
    an_list=[]
    for data in cluster_i:
        fo_dic = fo_map(data)
        if data not in fo_dic.keys():
            length=length-1
        else:
            an_list=an_list+fo_dic[data]
    if len(an_list)!=0:
        frequency=Counter(an_list)
        if max(frequency.values())==length:
            consistent=consistent+1
print('consistent=',consistent)
print('specificity=',consistent/cluster_number)




