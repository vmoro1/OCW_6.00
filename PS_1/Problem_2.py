#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 08:24:21 2019

@author: viggomoro
"""

s = 'azcbobobegghakl'
counter = 0

for i in range(len(s)):  
    if s[i:i + 3] == 'bob':
        counter += 1

print("The number of times bob occurs is " + str(counter))