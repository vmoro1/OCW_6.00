#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:35:52 2019

@author: viggomoro
"""

s = 'abcde'  # ska printa vokaler
counter = 0

for letter in s:
    while letter in ('a', 'e', 'i', 'o', 'u'):
        counter += 1
        break
        
print("The number of vowels is " + str(counter) )