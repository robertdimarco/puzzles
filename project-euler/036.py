# coding=utf-8

'''
Problem 36
31 January 2003

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

import euler
print sum(n for n in range(1, 10**6+1) if (euler.is_palindrome(n) and euler.is_palindrome(bin(n)[2:])))
