#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TItle : Multiplying list
Created : on Thu Apr 22 22:08:42 2021

@author: krigjo25
"""
def Multiple(x, li):
    
    for i, list in enumerate(li):
        li[i] = list * x
        print(li)              
    # Trying the function
        #Variables

li = [13, 15, 17, 19]
print(li)     
Multiple(4,li)
print(li)