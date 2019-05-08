# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:12:04 2019

@author: Administrator
"""
import re
def con_sim(name1,num1,name2,num2):
    file = open(r'G:/网络比对/实验结果_多网络/3网络数据/con_sim/' + name1+'-'+ name2 +'.evals','w')
    #print(name1,num1)
    for i in range(1,int(num1)):
        #print(i)
        for j in range(1,int(num2)):
            print("%s%d\t%s%d\t1.0\n" %(name1,i,name2,j))
            file.write("%s%d\t%s%d\t1.0\n" %(name1,i,name2,j))
    file.close()
    """file1 = open(r'G:/网络比对/实验结果_多网络/3网络数据/IID'+name2+'.gw','r')
    lines1 = file1.readlines()
    nrow = int(lines1[4])
    G =[]
    for i in range(5, nrow + 5):
        lineArr1 = lines1[i].strip('\n')
        lineArray1 = re.match(r'(.*?)\|{(.*?)\}|(.*?)', lineArr1).group(2)
        #print(lineArray)
        G.append(lineArray1)
    file1.close()
    file2 = open(r'G:/网络比对/实验结果_多网络/3网络数据/IID'+name1+'.gw','r')
    lines2 = file2.readlines()
    for j in range(5, nrow + 5):
        lineArr2 = lines2[j].strip('\n')
        lineArray2 = re.match(r'(.*?)\|{(.*?)\}|(.*?)', lineArr2).group(2)
        #print(type(lineArray2))
        for m in G:
            print(type(m))
            #file.write(lineArray2 + "\t"+ m + "\t1.0\n")
            file.write("%s\t%s\t1.0\n"% (lineArray2,m))
    file.close()"""

f = open(r'G:/网络比对/实验结果_多网络/3网络数据/list.txt','r')
lines = f.readlines()
for k in lines:
    lineARR = k.strip().split('-')
    con_sim(lineARR[0],lineARR[1],lineARR[2],lineARR[3])

