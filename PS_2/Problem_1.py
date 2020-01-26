#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:35:37 2019

@author: viggomoro
"""

def balance_mmp(balance = 42, annualInterestRate = 0.2, monthlyPaymentRate = 0.04):
    
    monthlyInterestRate = annualInterestRate / 12
    output = ''
    
    for i in range(1,13):
        MinimumPayment = balance * monthlyPaymentRate
        Intrest = (balance - MinimumPayment) * monthlyInterestRate
        balance += Intrest - MinimumPayment
        output += 'Month ' + str(i) + ' Remaining balance: ' + str(round(balance, 2)) + '\n'
        
    return output


#print(balance_mmp())


def balance_mmp_2(balance = 484, annualInterestRate = 0.2, monthlyPaymentRate = 0.04):
    
    monthlyInterestRate = annualInterestRate / 12
    
    for i in range(1,13):
        MinimumPayment = balance * monthlyPaymentRate
        Intrest = (balance - MinimumPayment) * monthlyInterestRate
        balance += Intrest - MinimumPayment
        print('Month ' + str(i) + ' Remaining balance: ' + str(round(balance, 2)))


#balance_mmp_2()
        

#def balance_mmp_recursive(balance, annualInterestRate, monthlyPaymentRate, months:
#    
#    monthlyInterestRate = annualInterestRate / 12
#    minpay = balance * monthlyPaymentRate
#    Intrest = (balance - minpay) * monthlyInterestRate
#    balance = balance + Intrest - minpay
#    
#    if months == 1:
#        return round(balance, 2)
#    else:
#        balance_mmp_recursive(balance, annualInterestRate, monthlyPaymentRate, months - 1)
#        
#
#print(balance_mmp_recursive(42, 0.2, 0.04, 12))
#        



def Balance(b,m,r,n):
    Ub0 = b - b*m
    b1 = Ub0 + Ub0*r/12 
    
    if n == 1:
        return b1
    else:                
        Balance(b1,m,r,n-1)
        
        
print(Balance(42,0.2,0.04,12))