import networkx as nx
import linecache
import time
time_start=time.time()
def read_network(path):
    G=nx.Graph()
    f = open(path, 'r')
    for lines in f.readlines():
        edge= lines.strip('\n').split('\t')
        G.add_edge(edge[0],edge[1])
    f.close()
    return G
G_hu=read_network('hu.tab')
G_mo=read_network('mo.tab')
G_rt=read_network('rt.tab')

file=open("09_10.txt","r")
cluster_num=len(file.readlines())#簇的数量

e_total=0
ecs_total=0
for i in range(0,cluster_num-1):#第一个到倒数第二个簇
    i_hu=[]# list of proteins of network : hu
    i_mo=[]
    i_rt=[]

    i_cluster=linecache.getline('09_10.txt',i+1)#簇的行数，从1开始计数
    i_cluster_data=i_cluster.strip('\n').split(' ')

    for data in i_cluster_data:
        if(data.startswith('hu')==1):# use 'is True' will be more readable
            i_hu.append(data)
        elif(data.startswith('rt')==1):
            i_rt.append(data)
        elif(data.startswith('mo')==1):
            i_mo.append(data)
    # cluster i's info

            
    for j in range(i+1,cluster_num):
        j_hu=[]
        j_mo=[]
        j_rt=[]
        s_hu=0
        s_mo=0
        s_rt=0
        s=0
        e=0

        j_cluster=linecache.getline('09_10.txt',j+1)
        j_cluster_data=j_cluster.strip('\n').split(' ')
        
        for datas in j_cluster_data:
            if(datas.startswith('hu')==1):
                j_hu.append(datas)
            if(datas.startswith('mo')==1):
                j_mo.append(datas)
            if(datas.startswith('rt')==1):
               j_rt.append(datas)
        # cluster (i+k)'s info

        for ihu in i_hu:
            for jhu in j_hu:
                if ((ihu,jhu) in G_hu.edges()) or ((jhu,ihu) in G_hu.edges()):
                    e=e+1
                    s_hu=1
        for imo in i_mo:
            for jmo in j_mo:
                if ((imo,jmo) in G_mo.edges()) or ((jmo,imo) in G_mo.edges()):
                    e=e+1
                    s_mo=1
        for irt in i_rt:
            for jrt in j_rt:
                if ((irt,jrt) in G_rt.edges() or (jrt,irt) in G_rt.edges()):
                    e=e+1
                    s_rt=1
        s_=s_hu+s_mo+s_rt#s'

        if len(i_hu)!=0 and len(j_hu)!=0:
            shu=1
        else:
            shu=0
        if len(i_mo)!=0 and len(j_mo)!=0:
            smo=1
        else:
            smo=0
        if len(i_rt)!=0 and len(j_rt)!=0:
            srt=1
        else:
            srt=0
        s=shu+smo+srt

        if (s_==1):
            cs=0
        else:
            cs=s_/s
        e_total=e_total+e
        es=e*cs
        ecs_total=ecs_total+es

CIQ=ecs_total/e_total
print("ecs_total:",ecs_total)
print("e_total:",e_total)
print ("CIQ:",CIQ)
file.close()
time_end=time.time()
print("totally cost：",time_end-time_start)
   
