#!/usr/bin/env python3.2 

import math

def IsPrime(num):
    if num < 1:
        return False
    for number in range(2, math.floor(math.sqrt(num) + 1)):
        if num % number == 0:
            return False
    return True
        
def GetPrime(limit):
    count = 0
    number = 1 
    while count < limit:
        number += 1
        if IsPrime(number):
            count += 1
    return number

print(GetPrime(10001))
