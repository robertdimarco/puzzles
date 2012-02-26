# coding=utf-8

from __future__ import division

if __name__ == "__main__":
  import importlib, sys, time
  start = time.time()
  importlib.import_module(sys.argv[1])
  finish = time.time()
  print "Time: " + str(round(finish - start, 4)) + "s"


# H(n) = n(2n-1)
def is_hexagonal(n):
  import decimal, math
  if n == 0: return False
  x = decimal.Decimal(str(0.25 + 0.25*math.sqrt(1 + 8*n)))
  print x
  return True if (x == int(x)) else False

def is_lychrel(n, iterations = 50):
  for i in range(iterations):
    n += int(str(n)[::-1])
    if is_palindrome(n):
     return False
  return True

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

# P(n) = n(3n-1)/2
# https://en.wikipedia.org/wiki/Pentagonal_number
def is_pentagonal(n):
  import decimal, math
  if n == 0: return False
  x = decimal.Decimal(str((1/6) + (1/3)*math.sqrt(0.25 + 6*n)))
  return True if (x == int(x)) else False

def is_permutation(a, b):
  return True if (sorted(str(a)) == sorted(str(b))) else False

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

def is_pythagorean_triple(a, b, c):
  if (a > 0) and (b > 0) and (c > 0):
    if (c**2 == (a**2 + b**2)):
      return True
  return False

# T(n) = n(n+1)/2
def is_triangle(n):
  import decimal, math
  if n == 0: return False
  x = decimal.Decimal(str(-0.5 + math.sqrt(0.25 + 2*n)))
  print x
  return True if (x == int(x)) else False


# Euler's Totient Function
def phi(n):
  import operator
  if is_prime(n): return n-1
  return n*reduce(operator.mul, map(lambda x: (x-1)/x, set(primefactors(n))))

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

def get_prime_factors(n):
  from math import sqrt
  i = 2
  while i<=sqrt(n):
    if n%i==0:
      l = get_prime_factors(n/i)
      l.append(int(i))
      return l
    i+=1
  return [int(n)]


class Totient:
  def __init__(self, n):
    self.totients = [1 for i in range(n)]
    for i in range(2, n):
      if self.totients[i] == 1:
        for j in range(i, n, i):
          self.totients[j] *= i - 1
          k = j / i
          while k % i == 0:
            self.totients[j] *= i
            k /= i
  def __call__(self, i):
    return self.totients[i]