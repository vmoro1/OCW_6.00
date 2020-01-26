#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:27:40 2019

@author: viggomoro
"""

def LowestPayment(balance, annualInterestRate):
    
    monthlyInterestRate = annualInterestRate / 12
    MonthlyPayment = 10
    balance1 = balance
    
    while balance1 > 0:
        balance1 = balance
        for i in range(1,13):
            Intrest = (balance1 - MonthlyPayment) * monthlyInterestRate
            balance1 += Intrest - MonthlyPayment
        if balance1 > 0:
            MonthlyPayment += 0.0001
            
        
    return MonthlyPayment


print(LowestPayment(4773, 0.2))
    
        

        
        