#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:11:37 2019

@author: viggomoro
"""
import string
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        assert type(other) == type(self)
        return (self.getX() == other.getX() and self.getY() == other.getY())
    
#    def __repr__:(self)
#        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
    
    
    
class intSet(object):
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        """Assumes other is an intSet
           Returns a new intSet containing elements that appear in both sets."""
        commonValueSet = intSet()
        for val in self.vals:   
            if other.member(val):
                commonValueSet.insert(val)
        return commonValueSet
    
#    def __len__(self):
#    """Returns the length of the set.
#       This method is called by the `len` built-in function."""
#       return len(self.vals)
        
        
class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")
        
#obj = D()
#
#print(obj.a)

    
def genPrimes():
    primes = []   
    last = 1     
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
