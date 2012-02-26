# coding=utf-8

'''
Problem 73
02 July 2004

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

  1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

Note: The upper limit has been changed recently.
'''

from __future__ import division
import euler, math, fractions
answer = set()
for i in range(1, 12001):
  n_min = int(math.floor((1/3)*i) + 1)
  n_max = int(math.ceil((1/2)*i) - 1)
  for j in range(n_min, n_max + 1):
    gcd = fractions.gcd(i, j)
    answer.add(str(j/gcd) + '/' + str(i/gcd))
print len(answer)
