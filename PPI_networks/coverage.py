# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 13:01:25 2019

@author: Administrator
"""
import networkx as nx
import re
"""
1.准备工作
"""
cluster = []
fs=open(r'G:/网络比对/实验结果_多网络/3网络数据/结果/c_3_ns.txt','r')#文件目录

def readgraph(filename):
    f = open(filename, "r")
    lines = f.readlines()
    G = nx.Graph()
    nrow = int(lines[4])
    for i in range(5,nrow+5):
        lineArr=lines[i].strip('\n')
        lineArray = re.match(r'(.*?)\|{(.*?)\}|(.*?)', lineArr).group(2)
        G.add_node(lineArray)
    erow = int(lines[5 + nrow])
    for j in range(nrow+6,nrow+erow+6):
        data = lines[j].strip().split(' ')
        if data[0]!=data[1]:
            G.add_edge(data[0],data[1])
    print(len(G.nodes()))
    return G
#读取网络数据
G1 = readgraph('G:/网络比对/实验结果_多网络/3网络数据/IIDhuman.gw')
G2 = readgraph('G:/网络比对/实验结果_多网络/3网络数据/IIDmouse.gw')
G3 = readgraph('G:/网络比对/实验结果_多网络/3网络数据/IIDrat.gw')

"""
2.计算coverage
"""
lines = fs.readlines()
protein = []
cluster_num=len(lines)
edge = []
specis = []

for i in lines:
    lineArr1=i.strip().split(' ')
    #lineArr1 = re.split('[ \t]',i)
    print(lineArr1)
    n = len(lineArr1)
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    while n!=0:  
        protein.append(lineArr1[n-1])
        n = n-1

print('number of cluster：' + cluster_num)
print('number of protien: ' + len(protein))


