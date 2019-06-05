# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:10:35 2019

@author: Administrator
"""

import numpy as np
import os
import math


def load_data(file_name):
    fr=open(file_name)
    eva_set=[]
    for line in fr.readlines():
        lineArr=line.rstrip().split('\t')
        eva_set.append(lineArr[2])
        
    fr.close()
    return eva_set


def file_name(file_dir):
    L=[]
    
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] =='.sim':
                L.append(os.path.join(root, file))
               # print(file)                                                      
    return L
    

def write_data(file_name,loge):
    f=open(file_name,'r+')
    #print(file_name[-9:])
    lineset=[]
    n=f.readlines()
    for line in range(len(n)):
        #print(loge[line])
        lineArr=n[line].rstrip().split('\t')      
        lineset.append([lineArr[0],lineArr[1],loge[line]])
    create_report(file_name,lineset)
    
       # print(lineset)
    f.close()    


def create_report(file_name,lineset):
    
    f_name='./log_evalue/'+file_name[-9:]
    f1=open(f_name,'w')
    #f1.write('a')
    #lineset=np.array(lineset)
    for i in range(len(lineset)):
        for j in range(3):
            f1.write(str(lineset[i][j])+'\t')
        f1.write('\n')
    f1.close()       
  
    
if __name__=='__main__' :
   
    file_dir='./sim_by_tab'
    L=file_name(file_dir)
    #print(L)   
    for i in range(len(L)):
        #print(file[i])        
        eva_set=load_data(L[i])        
        #eva_set.sort()
       # print(eva_set)
        logeva=[]
        
        for e in range(len(eva_set)):
            if eva_set[e]=='0.0':
                eva_set[e]=math.log(1e-323)
                log_eva=eva_set[e]
            else:
                log_eva=math.log(float(eva_set[e]))
                 
            logeva.append(log_eva)
        loge=np.array(logeva)            
      #  print(loge)
        write_data(L[i],loge)
      
    print("计算完成！")            
 
      

    
    
    
    
    
    