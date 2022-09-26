# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:50:07 2022

@author: edbin
"""
parola = ['radar', 'anna', 'affogalagoffa', 'ireneri' ,'itopononavevanonipoti','palindromo','buongiorno']


def palindroma_iter(parola):
    #return parola == parola[::-1]:
    for i in range(len(parola//2)):
        if parola[i] != parola[-i-1]:
            return False
    return True

def palindroma_rico(parola):
    if len(parola) <=1:
        return True
    if parola[0] == parola[-1]:
        return palindroma_rico(parola[1:-1])
    else:
        pass
    
def fibonacci(n):
    if 0<=n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    