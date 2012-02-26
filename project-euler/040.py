# coding=utf-8

'''
Problem 40
28 March 2003

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12^(th) digit of the fractional part is 1.

If d_(n) represents the n^(th) digit of the fractional part, find the value of the following expression.

d_(1) × d_(10) × d_(100) × d_(1000) × d_(10000) × d_(100000) × d_(1000000)
'''

import operator
i, j, substr = 0, 0, ""
while j < 10**6:
  i += 1
  substr += str(i)
  j += len(str(i))
print reduce(operator.mul, [int(substr[10**k-1]) for k in range(0, 7)])
