# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:40:25 2019

@author: cy
"""
#3iid
from collections import defaultdict
import networkx as nx
#import linecache
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

#file=open("09_10.txt","r")

file=open("alignment.txt","r")
cluster_num=len(file.readlines())#簇的数量
d=defaultdict(list)#字典
c_time=0#1.计数cluster行数；2.用作字典key值
try:
    with open('alignment.txt','r') as dict_file:#读alignment文件
        for line in dict_file:
            sample_=line.strip('\n').split(' ')#读alignment文件中每一行line
            for sample in sample_:#遍历list变量sample_中每个元素
                d[c_time].append(sample)#将sample加入key值为c_time的字典中
            c_time=c_time+1
except IOError as ioerr:
    c_time=c_time+1


e_total=0
ecs_total=0
for i in range(0,cluster_num-1):#第一个到倒数第二个簇
    i_hu=[]
    i_mo=[]
    i_rt=[]
    
    i_cluster=d[i]
#    i_cluster_data=i_cluster.strip('\n').split(' ')
#    i_cluster=linecache.getline('09_10.txt',i+1)#簇的行数，从1开始计数
    for data in i_cluster:
        if(data.startswith('hu')==1):
            i_hu.append(data)
        elif(data.startswith('rt')==1):
            i_rt.append(data)
        elif(data.startswith('mo')==1):
            i_mo.append(data)

            
    for j in range(i+1,cluster_num):
        j_hu=[]
        j_mo=[]
        j_rt=[]
        s_hu=0
        s_mo=0
        s_rt=0
        s=0
        e=0
        
        j_cluster=d[j]

#        j_cluster=linecache.getline('09_10.txt',j+1)
#        j_cluster_data=j_cluster.strip('\n').split(' ')
        
        for datas in j_cluster:
            if(datas.startswith('hu')==1):
                j_hu.append(datas)
            if(datas.startswith('mo')==1):
                j_mo.append(datas)
            if(datas.startswith('rt')==1):
               j_rt.append(datas)
        
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
            if(s==0):
                s=1
            cs=s_/s
        e_total=e_total+e
        es=e*cs
        ecs_total=ecs_total+es
if(e_total==0):
    e_total=1
CIQ=ecs_total/e_total
print("ecs_total:",ecs_total)
print("e_total:",e_total)
print ("CIQ:",CIQ)
file.close()
time_end=time.time()
print("totally cost：",time_end-time_start)

