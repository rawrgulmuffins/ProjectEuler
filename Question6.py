#!/usr/bin/env python3.2

import math
def getSumOfSquares(limit):
    sum = 0
    for ix in range(1, limit + 1):
        sum += ix**2
    return sum

        
def getSquareOfSums(limit):
    sum = 0
    for ix in range(1, limit + 1):
        sum += ix
    sum = sum**2
    return sum

print(getSquareOfSums(100) - getSumOfSquares(100))
