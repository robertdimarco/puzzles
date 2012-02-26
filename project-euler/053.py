# coding=utf-8

'''
Problem 53
26 September 2003

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5 choose 3 = 10.

In general, n choose r = n! / (r!(n−r)!), where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23 choose 10 = 1144066.

# How many, not necessarily distinct, values of n choose r, for 1 ≤ n ≤ 100, are greater than one-million?
'''

import math
def choose(n,r):
  return math.factorial(n) / (math.factorial(r)*math.factorial(n-r))
print sum(1 for n in range(1, 101) for r in range(n+1) if choose(n, r) > 10 ** 6)
