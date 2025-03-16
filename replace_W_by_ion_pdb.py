# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 13:02:58 2025

@author: wangz
"""
import numpy as np
from collections import deque


def get_random_line_number(start,end,number):
    start=int(start)
    end=int(end)
    if number > (end - start + 1):
        raise ValueError("make sure that n is smaller than a-b ")
    list=np.random.choice(np.arange(start, end+1), size=number, replace=False)
    list.sort()
    return list

def extract(file,newfile_W,newfile_ions,n_list):
    n_list=[i-1 for i in n_list]
    
    with open(file, "r") as file:
        lines = file.readlines()
        
    np.random.shuffle(n_list)
    extracted_lines = [lines[i] for i in n_list]
    
    with open(newfile_ions, "w") as file:
        file.writelines(extracted_lines)
    
    n_list.sort()
    n_list_reverse=n_list[::-1]
    for i in n_list_reverse:
        del lines[i]

    with open(newfile_W, "w") as file:
        file.writelines(lines)
    
    

def modify(line,new_atom_name,index_list):
    coordinate_x=float(line[30:38])
    coordinate_y=float(line[38:46])
    coordinate_z=float(line[46:54])
    w_coordinate_list=[coordinate_x,coordinate_y,coordinate_z]
    line_new="ATOM  {0:>5d}  {1:<3s} {2:<4s}{3:>1s}{4:>4d}    {5:>8.3f}{6:>8.3f}{7:>8.3f}  0.00  0.00           {8}"\
                        .format(index_list[0],new_atom_name,new_atom_name,"X",index_list[1],w_coordinate_list[0]\
                                ,w_coordinate_list[1],w_coordinate_list[2]," ")
    return line_new

'''def last_index(file):#get index
    with open(file, "r") as file:
        last_line = deque(file, maxlen=1).pop()
    index1=int(last_line[5:11])
    index2=int(last_line[22:26])
    
    index_list=[index1,index2]
    
    if all(element.isspace() for element in index_list):
        index_list=[-1,-1]
        
    return index_list'''

line_start_end=input("input the start and end line index(from1)")
line_start_end_list=line_start_end.split()
file_name="6664dope_remove_water.pdb" 

number=int(input("how many water you wannna remove"))
atom_name1=input("what atom1 you wanna replace with")
atom_name2=input("what atom2 you wanna replace with")

line_list=get_random_line_number(line_start_end_list[0],line_start_end_list[1], number)

index_list=[0,0]

extract(file_name,"newfile_W.pdb","newfile_ions.pdb",line_list)

with open("newfile_ions.pdb","r") as newfile_ions:
    lines=newfile_ions.readlines()

with open("newfile_ions_renew.pdb","w") as newfile_ions_renew:
    for line in lines:
        index_list=[i+1 for i in index_list]
        if index_list[0] <= (number/2): 
            newfile_ions_renew.write(modify(line,atom_name1,index_list)+"\n")
        elif index_list[0] > (number/2): 
            newfile_ions_renew.write(modify(line,atom_name2,index_list)+"\n")

























