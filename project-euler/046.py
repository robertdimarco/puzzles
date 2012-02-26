# coding=utf-8

'''
Problem 46
20 June 2003

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^(2)
15 = 7 + 2×2^(2)
21 = 3 + 2×3^(2)
25 = 7 + 2×3^(2)
27 = 19 + 2×2^(2)
33 = 31 + 2×1^(2)

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

import euler, math
primes = dict.fromkeys(euler.prime_sieve(10**4), True)
for i in range(3, 10**4, 2):
  if i in primes:
    continue
  valid = False
  for j in range(2, i):
    k = math.sqrt((i-j)/2)
    if (j in primes) and (int(k) == k):
      valid = True
  if not (valid):
    print i
    break
