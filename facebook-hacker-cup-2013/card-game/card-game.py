#!/usr/bin/env python

import sys

def nchoosek(n, k):
  if k < 0 or k > n:
    return 0
  elif k > (n - k):
    k = n - k

  c = 1
  for i in range(0, k):
    c = c * (n - (k - (i+1)))
    c = (c / (i+1))
  return c

t = int(sys.stdin.readline())
for i in range(1, t+1):
  n, k = [int(x) for x in sys.stdin.readline().strip().split(' ')]
  a = [int(x) for x in sys.stdin.readline().strip().split(' ')]
  a.sort(reverse=True)

  binomial, total = nchoosek(n, k), 0
  for j in range(n-k+1):
    diff = nchoosek(n-j, k) - nchoosek(n-j-1, k)
    total += a[j] * diff % 1000000007
  print 'Case #%d: %d' % (i, total)
  