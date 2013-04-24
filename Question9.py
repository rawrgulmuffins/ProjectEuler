#!/usr/bin/env python3.2 

import math


def ProduceC(A, B):
    C = A**2 + B**2
    return math.sqrt(C)

def FindTriplet(target):
    for A in range(1, target):
        for B in range(A + 1, target):
            C = ProduceC(A, B)
            if C + A + B == target:
                return A, B, C
    return None

print(FindTriplet(1000))
