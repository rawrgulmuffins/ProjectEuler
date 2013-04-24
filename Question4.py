#!/usr/bin/env python3.2

def IsPalindrome(number):
    num = str(number)
    if len(num) == 1:
        return True
    for ix in range(len(num) // 2):
        if(num[ix] != num[len(num) - ix - 1 ]):
            return False
    return True

def FindLargestPalindrome():
    largest_palindrome = 0
    for ix in range(999):
        for jx in range(999):
            if IsPalindrome(jx * ix):
                if jx * ix > largest_palindrome:
                    largest_palindrome = jx * ix
    return largest_palindrome

print(FindLargestPalindrome())
