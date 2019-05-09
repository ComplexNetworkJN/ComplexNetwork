# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:22:02 2019

@author: Administrator
"""
name=input("Input similarity file's Name")


read = open(f'{name}.evals','r')
write = open(f'new_{name}.evals','w')

file = read.readlines()

for i in file:
    lineArr = i.strip().split(' ')
    write.write(lineArr[0]+'\t'+lineArr[1]+'\t'+ '1.0' + '\n')

read.close()
write.close()
