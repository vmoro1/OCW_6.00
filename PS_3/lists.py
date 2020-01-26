#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:05:48 2019

@author: viggomoro
"""

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L
        

def plusone(a):
    a += 1
    return a

#print(applyToEach(testList, plusone))



def square(a):
    return a ** 2


print(applyToEach(testList, square))