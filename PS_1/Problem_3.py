#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:04:07 2019

@author: viggomoro
"""

s = 'azcbobobegghakl' #längsta alfabetiska fallande ordning ex. beegh
sequense = ''
counter = 0


for i in range(len(s)):
    if i <= (len(s) - 2):
        if s[i] <= s[i + 1]:
            sequense += s[i]
        else:
            sequense += s[i]
            sequense += ' '
    else:
        sequense += ' '
        sequense += s[(len(s) - 1)]
        
        
for index in range(len(sequense)):
    while sequense[index] == ' ':
        if counter == 0:
            longest_sequense = sequense[:index]
        elif ((index - 1) - counter) > len(longest_sequense):
            longest_sequense = sequense[counter + 1:index]
        counter = index
        break
            
        
print(longest_sequense)            