# coding=utf-8

'''
Problem 58
05 December 2003

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

  37 36 35 34 33 32 31
  38 17 16 15 14 13 30
  39 18  5  4  3 12 29
  40 19  6  1  2 11 28
  41 20  7  8  9 10 27
  42 21 22 23 24 25 26
  43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''

from __future__ import division
import euler
n = 0
ratio = d = x = 1
def corner_primes(n):
  if n <= 0:
    return 0
  return euler.is_prime(4*(n-1)**2+1) + euler.is_prime(4*n**2-10*n+7) + euler.is_prime(4*n**2-6*n+3)
while ratio > 0.10:
  x += 1
  n += corner_primes(x)
  d += 4
  ratio = n/d
print 2*x-1
