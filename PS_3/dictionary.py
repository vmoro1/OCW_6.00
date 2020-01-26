#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:14:08 2019

@author: viggomoro
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}
#print(animals.keys())

def how_many(aDict):
    counter = 0
    for i in aDict:
        counter += len(aDict[i])
    
    return counter


#print(how_many(animals))


def biggest(aDict):

    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result     


#print(biggest(animals))