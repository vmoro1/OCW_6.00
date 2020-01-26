#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:05:48 2019

@author: viggomoro
"""

def oddTuples(aTup):
    #return aTup[::2]
    oddTup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            oddTup += (aTup[i],)
    return oddTup



print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))