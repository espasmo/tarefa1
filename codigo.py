# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:42:39 2022

@author: bruno
"""

def abb(line):
    s = "s0"
    for letra in line:
        if s == "s0" and letra == 'c':
            s = "Morte"
        elif s == "s0" and letra == 'b':
            s = "s0"
        elif s == "s0" and letra == 'a':
            s = "s0b"
        elif s == 'Morte' and letra == 'c':
            s = "Morte"
        elif s == 'Morte' and letra == 'b':
            s = "Morte"
        elif s == 'Morte' and letra == 'a':
            s = "Morte"
        elif s == 's0b' and letra == 'c':
            s = "Morte"
        elif s == 's0b' and letra == 'b':
            s = "s1b"
        elif s == 's0b' and letra == 'a':
            s = "Morte" 
        elif s == 's1b' and letra == 'c':
            s = "Morte"
        elif s == 's1b' and letra == 'b':
            s = "s0"
        elif s == 's1b' and letra == 'a':
            s = "Morte"
        elif letra != '\n':
            return("nao pertencimento")
    if (s == "s0"):
        return("pertencimento")
    else:
        return("nao pertencimento")
        

with open('teste3.txt') as f:
    lines = f.readlines()
    for line in lines:
        print(abb(line))
    
    