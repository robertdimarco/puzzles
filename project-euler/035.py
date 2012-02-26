# coding=utf-8

'''
Problem 35
17 January 2003

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import euler
primes = dict.fromkeys(euler.prime_sieve(10**6), True)
def is_circular_prime(n):
  x = str(n)
  for i in range(0, len(x)):
    if int(x[i:] + x[:i]) not in primes:
      return False
  return True
print sum(1 for n in primes if is_circular_prime(n))
