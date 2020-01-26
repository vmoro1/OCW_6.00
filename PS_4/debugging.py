#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:02:18 2019

@author: viggomoro
"""

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count


#print(integerDivision(7, 5))
    
def divide(numbers,index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
        
        
#divide([0, 2, 4], 0)
        

def division(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   try:
       return item / denom
   except ZeroDivisionError:
       return 0
   

#print(division([0, 2, 4], 0))