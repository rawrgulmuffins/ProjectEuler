#!/usr/bin/env python3.2


def fibio(limit, summation,  previous, current):
    if previous > limit:
        return summation
    if previous % 2 == 0:
        summation += previous
    print(previous, current, summation)
    return fibio(limit, summation, current, current + previous)
    
sum = 0

sum = fibio(4000000, sum, 1, 2)

print(sum)


