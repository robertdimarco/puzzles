# coding=utf-8

'''
Problem 43
09 May 2003

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d_(1) be the 1^(st) digit, d_(2) be the 2^(nd) digit, and so on. In this way, we note the following:

    * d_(2)d_(3)d_(4)=406 is divisible by 2
    * d_(3)d_(4)d_(5)=063 is divisible by 3
    * d_(4)d_(5)d_(6)=635 is divisible by 5
    * d_(5)d_(6)d_(7)=357 is divisible by 7
    * d_(6)d_(7)d_(8)=572 is divisible by 11
    * d_(7)d_(8)d_(9)=728 is divisible by 13
    * d_(8)d_(9)d_(10)=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

import itertools
primes = [2,3,5,7,11,13,17]
def p043(n):
  n = int(''.join(n))
  return False if sum(1 for i in range(1,8) if (int(str(n)[i:i+3]) % primes[i-1] != 0)) else True
print sum(int(''.join(i)) for i in itertools.permutations(str(9876543210), 10) if p043(i))
