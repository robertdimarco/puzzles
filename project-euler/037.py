# coding=utf-8

'''
Problem 37
14 February 2003

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import euler
def truncatable_prime(n):
  if n < 10: return False
  for i in range(1, len(str(n))):
    if not euler.is_prime(int(str(n)[i:])) or not euler.is_prime(int(str(n)[:-i])):
      return False
  return True
print sum(i for i in euler.prime_sieve(10**6) if truncatable_prime(i))
