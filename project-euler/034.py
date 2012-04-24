# coding=utf-8

'''
Problem 34
03 January 2003

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math
facts = [math.factorial(i) for i in range(10)]
def sumfact(n):
  return (sum(facts[int(i)] for i in str(n)) == n)
print sum(i for i in range(3, 10**5) if sumfact(i))
