# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:12:04 2019

@author: Administrator
"""

def con_sim(name1,num1,name2,num2):
    file = open(f'{name}.evals','w')
    for i in range(0,int(num1)):
    
        for j in range(0,int(num2)):
            #print("%s%d\t%s%d\t1.0\n" %(name1,i,name2,j))
            file.write("%s%d\t%s%d\t1.0\n" %(name1,i,name2,j))
    file.close()

name=input("Input species' name:\n")
num1,num2 = input("Input number of nodes:\n").split(',')

lineARR = name.split('-')
name1 = lineARR[0]
name2 = lineARR[1]
con_sim(name1[0:2],num1,name2[0:2],num2)

