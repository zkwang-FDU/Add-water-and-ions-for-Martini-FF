# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:30:36 2025

@author: zkwang
"""
import numpy as np
from collections import deque
import re

def split_coordinates(c):#put coordinate into list
    c_list_n=[]
    c_list=c.split()
    for i in c_list:
        c_list_n.append(float(i))
    return c_list_n

def side_length(c1_list,c2_list):#compute side length
    a=abs(c1_list[1]-c2_list[1])
    b=abs(c1_list[1]-c2_list[1])
    c=abs(c1_list[2]-c2_list[2])
    return [a,b,c]

def volume(side_lenth):#compute volume
    V=1
    for i in side_lenth:
        V=V*i
    return V

def lattice_number_split(side_lenth,number):#let user input lattice length untill satisfied
    i=1
    n=0
    while True:
        i=float(input("pls input lattice_length:"))
        n=(side_lenth[0]//i)*\
        (side_lenth[1]//i)*\
        (side_lenth[2]//i)
        print(n)
        
        tag=input("wheather you are satisfied?[y/n]")
        if tag=="y":
            break
        
    return i

def last_index(file):#get index
    with open(file, "r") as file:
        last_line = deque(file, maxlen=1).pop()
    index1=int(last_line[5:11])
    index2=int(last_line[22:26])
    
    index_list=[index1,index2]
    return index_list

def line(index_list,w_coordinate_list):#standard line format of PDB
    line="ATOM  {0:>5d}  {1:<3s} {2:<4s}{3:>1s}{4:>4d}    {5:>8.3f}{6:>8.3f}{7:>8.3f}  0.00  0.00           {8}"\
                        .format(index_list[0],"W","W","X",index_list[1],w_coordinate_list[0]\
                                ,w_coordinate_list[1],w_coordinate_list[2]," ")
    return line


c1=input("pls input coordinate1,make sure that 2>1:")
c2=input("pls input coordinate2,make sure that 2>1:")

c1_list=split_coordinates(c1)
c2_list=split_coordinates(c2)

side_length_list=side_length(c1_list, c2_list)

number=int(input("how much W you wanna add:"))#put your file name here

i=lattice_number_split(side_length_list, number)

filename="rm_all_water_rw_backup.pdb"
last_index_list=last_index(filename)



tag=0 
for a in np.arange(c1_list[0],c2_list[0],i):
    for b in np.arange(c1_list[1],c2_list[1],i):
        for c in np.arange(c1_list[2],c2_list[2],i):
            with open(filename, "a") as file:
                tag=tag+1
                last_index_list_renew=[int(x)+tag for x in last_index_list]
                while last_index_list_renew[0] >99999:
                    last_index_list_renew[0]=last_index_list_renew[0]-100000
                while last_index_list_renew[1] >9999:
                    last_index_list_renew[1]=last_index_list_renew[1]-10000
                file.write("\n"+line(last_index_list_renew, [round(a,3),round(b,3),round(c,3)]))






