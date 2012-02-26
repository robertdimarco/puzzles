# coding=utf-8

'''
Problem 47
04 July 2003

The first two consecutive numbers to have two distinct prime factors are:

  14 = 2 × 7
  15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

  644 = 2² × 7 × 23
  645 = 3 × 5 × 43
  646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
'''

import euler
factors = dict.fromkeys([1], 0)
for i in range(10**6):
  factors[i] = len(set(euler.get_prime_factors(i)))
  if (factors[i] == 4) and (factors[i-1] == 4) and (factors[i-2] == 4) and (factors[i-3] == 4):
    print i -3
    break
