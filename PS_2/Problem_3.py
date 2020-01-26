#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:05:59 2019

@author: viggomoro
"""

def LowestPayment_bisectionsearch(balance, annualInterestRate):
    
    monthlyInterestRate = annualInterestRate / 12
    payment_low = balance / 12
    payment_high = (balance * (1 + monthlyInterestRate) ** 12) / 12
    balance1 = balance
    
    while abs(balance1) > 0.01:
        MonthlyPayment = (payment_low + payment_high) / 2
        balance1 = balance
        for i in range(1,13):
            Intrest = (balance1 - MonthlyPayment) * monthlyInterestRate
            balance1 += Intrest - MonthlyPayment
        if balance1 >= 0.01:
            payment_low = MonthlyPayment
        elif balance1 <= 0.01:
            payment_high = MonthlyPayment
    
    return round(MonthlyPayment, 2)


print(LowestPayment_bisectionsearch(999999, 0.18))