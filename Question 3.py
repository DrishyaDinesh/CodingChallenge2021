import math
import os
import random
import re
import sys

def portfolio_profit_maximisation(maxSum, a, b):
    atop=0
    btop=0
    profit=0
    count=0
    while profit<=maxSum and atop<len(a) and btop<len(b):
        if a[atop]<b[btop] :
            profit+=a[atop]
            atop+=1
        else:
            profit+=b[btop]
            btop+=1
        if profit>maxSum:
            break
        else:
            count+=1
        
    while profit<=maxSum and atop==len(a) and btop<len(b):
        profit+=b[btop]
        btop+=1
        count+=1
    while profit<=maxSum and btop==len(a) and atop<len(a):
        profit+=a[atop]
        atop+=1
        count+=1
    
    return count
