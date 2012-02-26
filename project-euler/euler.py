# coding=utf-8

from __future__ import division

if __name__ == "__main__":
  import importlib, sys, time
  start = time.time()
  importlib.import_module(sys.argv[1])
  finish = time.time()
  print "Time: " + str(round(finish - start, 4)) + "s"


def is_palindrome(val):
  value = str(val)
  return True if value == value[::-1] else False

def is_pandigital(n):
  if not isinstance(n, (str, int)):
    n = ''.join(n)
  if (len(str(n)) > 9):
    return False
  compare_to = sum(i*(10**(i-1)) for i in range(1,len(str(n))+1))
  return True if (sorted(str(n)) == sorted(str(compare_to))) else False

def is_pythagorean_triple(a, b, c):
  if (a > 0) and (b > 0) and (c > 0):
    if (c**2 == (a**2 + b**2)):
      return True
  return False

# Sieve of Eratosthenes
def prime_sieve(n):
  primes = []
  is_prime = [False] * 2 + [True] * (n - 1)
  for i in range(n + 1):
    if is_prime[i]:
      primes.append(i)
      for j in range(i*i, n + 1, i):
        is_prime[j] = False
  return primes

def is_prime(n):
  if n <= 1: return False
  import math
  n = abs(n)
  i = 2
  while i <= math.sqrt(n):
    if n % i == 0:
      return False
    i += 1
  return True
