# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:40:25 2019

@author: cy
"""
#11iid
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
G_co=read_network('co.tab')
G_do=read_network('do.tab')
G_ho=read_network('ho.tab')
G_ca=read_network('ca.tab')
G_ra=read_network('ra.tab')
G_pi=read_network('pi.tab')
G_sh=read_network('sh.tab')
G_gu=read_network('gu.tab')

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
    i_co=[]
    i_do=[]
    i_ho=[]
    i_ca=[]
    i_ra=[]
    i_pi=[]
    i_sh=[]
    i_gu=[]

    i_cluster=d[i]#读取key值为i的字典中内容，及alignment文件第i行

    for data in i_cluster:
        if(data.startswith('hu')==1):
            i_hu.append(data)
        elif(data.startswith('rt')==1):
            i_rt.append(data)
        elif(data.startswith('mo')==1):
            i_mo.append(data)
        elif(data.startswith('co')==1):
            i_co.append(data)
        elif(data.startswith('do')==1):
            i_do.append(data)
        elif(data.startswith('ho')==1):
            i_ho.append(data)
        elif(data.startswith('ca')==1):
            i_ca.append(data)
        elif(data.startswith('ra')==1):
            i_ra.append(data)
        elif(data.startswith('pi')==1):
            i_pi.append(data)
        elif(data.startswith('sh')==1):
            i_sh.append(data)
        elif(data.startswith('gu')==1):
            i_gu.append(data)

            
    for j in range(i+1,cluster_num):
        j_hu=[]
        j_mo=[]
        j_rt=[]
        j_co=[]
        j_do=[]
        j_ho=[]
        j_ca=[]
        j_ra=[]
        j_pi=[]
        j_sh=[]
        j_gu=[]
        s_hu=0
        s_mo=0
        s_rt=0
        s_co=0
        s_do=0
        s_ho=0
        s_ca=0
        s_ra=0
        s_pi=0
        s_sh=0
        s_gu=0
        s=0
        e=0

        j_cluster=d[j]
        
        for datas in j_cluster:
            if(datas.startswith('hu')==1):
                j_hu.append(datas)
            if(datas.startswith('mo')==1):
                j_mo.append(datas)
            if(datas.startswith('rt')==1):
               j_rt.append(datas)
            if(datas.startswith('co')==1):
               j_co.append(datas)
            if(datas.startswith('do')==1):
               j_do.append(datas)
            if(datas.startswith('ho')==1):
               j_ho.append(datas)
            if(datas.startswith('ca')==1):
               j_ca.append(datas)
            if(datas.startswith('ra')==1):
               j_ra.append(datas)
            if(datas.startswith('pi')==1):
               j_pi.append(datas)
            if(datas.startswith('sh')==1):
               j_sh.append(datas)
            if(datas.startswith('gu')==1):
               j_gu.append(datas)
        
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
        for ico in i_co:
            for jco in j_co:
                if ((ico,jco) in G_co.edges() or (jco,ico) in G_co.edges()):
                    e=e+1
                    s_co=1
        for ido in i_do:
            for jdo in j_do:
                if ((ido,jdo) in G_do.edges() or (jdo,ido) in G_do.edges()):
                    e=e+1
                    s_do=1
        for iho in i_ho:
            for jho in j_ho:
                if ((iho,jho) in G_ho.edges() or (jho,iho) in G_ho.edges()):
                    e=e+1
                    s_ho=1
        for ica in i_ca:
            for jca in j_ca:
                if ((ica,jca) in G_ca.edges() or (jca,ica) in G_ca.edges()):
                    e=e+1
                    s_ca=1
        for ira in i_ra:
            for jra in j_ra:
                if ((ira,jra) in G_ra.edges() or (jra,ira) in G_ra.edges()):
                    e=e+1
                    s_ra=1
        for ipi in i_pi:
            for jpi in j_pi:
                if ((ipi,jpi) in G_pi.edges() or (jpi,ipi) in G_pi.edges()):
                    e=e+1
                    s_pi=1
        for ish in i_sh:
            for jsh in j_sh:
                if ((ish,jsh) in G_sh.edges() or (jsh,ish) in G_sh.edges()):
                    e=e+1
                    s_sh=1
        for igu in i_gu:
            for jgu in j_gu:
                if ((igu,jgu) in G_gu.edges() or (jgu,igu) in G_gu.edges()):
                    e=e+1
                    s_gu=1
        s_=s_hu+s_mo+s_rt+s_co+s_do+s_ho+s_ca+s_ra+s_pi+s_sh+s_gu#s'

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
        if len(i_co)!=0 and len(j_co)!=0:
            sco=1
        else:
            sco=0
        if len(i_do)!=0 and len(j_do)!=0:
            sdo=1
        else:
            sdo=0
        if len(i_ho)!=0 and len(j_ho)!=0:
            sho=1
        else:
            sho=0
        if len(i_ca)!=0 and len(j_ca)!=0:
            sca=1
        else:
            sca=0
        if len(i_ra)!=0 and len(j_ra)!=0:
            sra=1
        else:
            sra=0
        if len(i_pi)!=0 and len(j_pi)!=0:
            spi=1
        else:
            spi=0
        if len(i_sh)!=0 and len(j_sh)!=0:
            ssh=1
        else:
            ssh=0
        if len(i_gu)!=0 and len(j_gu)!=0:
            sgu=1
        else:
            sgu=0
        s=shu+smo+srt+sco+sdo+sho+sca+sra+spi+ssh+sgu

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








