#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:54:08 2019

@author: viggomoro
"""

number = int(input("Please think of a number between 0 and 100!"))

high = 100
low = 0
guess = (high + low) / 2
number_guesses = 0

while guess != number:
    if guess > number:
        high = guess
    else:
        low = guess
    number_guesses += 1
    guess = int((high + low) / 2)
    print(guess)
    
print("Your secret number was", str(guess))