# coding=utf-8

'''
Problem 50
15 August 2003

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import euler
primes = euler.prime_sieve(10**4)
longest = primesum = 1
for i in range(len(primes)):
  for j in range(i+longest, len(primes)):
    if (sum(primes[i:j]) < 10**6) and euler.is_prime(sum(primes[i:j])):
      longest = j-i
      primesum = sum(primes[i:j])
print primesum
