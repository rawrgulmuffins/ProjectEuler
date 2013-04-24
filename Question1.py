#!/usr/bin/env python3.2

sum = 0

for ix in range(1000):
    if ix * 3 >= 1000:
        break
    print(ix * 3)
    sum += ix * 3

for ix in range(1000):
    if ix * 5 >= 1000:
        break
    if (ix * 5) % 3 == 0:
        continue
    print(ix * 5)
    sum += ix * 5

print(sum)

