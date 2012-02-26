# coding=utf-8

'''
Problem 49
01 August 2003

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

import euler, collections, itertools, math
prime_sets = collections.defaultdict(list)
for prime in euler.prime_sieve(10**4):
  if (prime > 1000):
    key = tuple(sorted(str(prime)))
    prime_sets[key].append(prime)
for prime_set in prime_sets.itervalues():
  if (len(prime_set) >= 3):
    for pset in itertools.permutations(prime_set, 3):
      if (pset[2]-pset[1] == pset[1]-pset[0]) and (pset[0] < pset[1]):
        print ''.join(str(i) for i in pset)
