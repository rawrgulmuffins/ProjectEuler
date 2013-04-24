#!/usr/bin/env python3.2

def IsEvenlyDivisible(target, limit):
    if target < limit:
        return False
    for ix in range(2, limit):
        if target % ix != 0:
            return False
    return True

def FindSmallestDivisible():
    number = 2520
    while True:
        if IsEvenlyDivisible(number, 20):
            return number
        number += 10

print(FindSmallestDivisible())
