#!/usr/bin/env python3.2 

import math

def IsPrime(num):
    if num < 1:
        return False
    for number in range(2, num):
        #this function can be optimized by setting a break if number is
        #greater than sqrt(num)
       # print(num,number, num % number)
        if num % number == 0:
            return False
    return True
        
def GetPrimeFactors(target, PrimeFactors):
    if(IsPrime(target)):
        PrimeFactors.add(target)
        return
    for number in range(2, target):
        if target % number == 0:
            GetPrimeFactors(target // number, PrimeFactors)
            GetPrimeFactors(number, PrimeFactors)
            break
                
Primes = set()
GetPrimeFactors(600851475143, Primes)

#GetPrimeFactors(2, Primes)

for nums in Primes:
    print(nums)
    
