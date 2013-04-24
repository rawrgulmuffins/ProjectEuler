#!/usr/bin/env python3.2 

def FindLargest():
    LastDigits = [0, 0, 0, 0, 0]
    sum = 0
    ix = 0
    file_index = 0
    r_file = open("input")
    numbers = r_file.readline()
    while len(numbers) != 0:
        print(numbers[file_index])
        if(numbers[file_index] == '\n'):    
            file_index = 0
            numbers = r_file.readline()
            continue
        LastDigits[ix] = int(numbers[file_index])
        print(LastDigits, MulitiplyList(LastDigits))
        if MulitiplyList(LastDigits) > sum:
            sum = MulitiplyList(LastDigits)
        file_index += 1
        ix += 1
        if ix == 5:
            ix = 0
    return sum
        
def SumList(numbers):
    sum = 0
    for ix in range(len(numbers)):
        sum += numbers[ix]
    return sum


def MulitiplyList(numbers):
    product = 1 
    for ix in range(len(numbers)):
        product *= numbers[ix]
    return product

print(FindLargest())
