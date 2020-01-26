#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 17:10:44 2019

@author: viggomoro
"""

def iterPower(base, exp):
    
    value = 1
    counter = 1
    
    while counter <= exp:
        value *= base
        counter += 1
        
    return value

#print(iterPower(-2, 3))
    
def recurPower(base, exp):
    
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
    
#print(recurPower(-2,3))
        
    
def gcdIter(a, b):
    guess = min(a, b)
    
    for i in reversed(range(1, guess + 1)):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
            
    return gcd
    
#print(gcdIter(4,8))
    
def gcdRecur(a, b):
    
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

   
def isIn(char, aStr):
    
    if '' == 0:
          return False
    if len(aStr) == 1:
          return char == aStr
      
    midIndex = len(aStr) // 2
    midChar = aStr[midIndex]
    
    if char == midChar:
        return True
    elif char < midChar:
        return isIn(char, aStr[:midIndex])
    else:
        return isIn(char, aStr[midIndex + 1:])
    
#print(isIn('b', 'acdefghijklmn'))
    
    
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

#print("")
#print('Is eve a palindrome?')
#print(isPalindrome('eve'))
#
#print('')
#print('Is able was I ere I saw Elba a palindrome?')
#print(isPalindrome('Able was I, ere I saw Elba'))    