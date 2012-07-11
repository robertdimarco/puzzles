#!/usr/bin/env python

# expected time per attempt is given by equation
# time = L[0] + (1-P[0])*L[1] + (1-P[0])*(1-P[1])*L[2] + ...
# where L is the expected time and P is the probability of failure, per level
# swap two levels if L[i]*P[i+1] > L[i+1]*P[i]

import sys

if len(sys.argv) < 2:
  sys.exit('Usage: %s file.in' % sys.argv[0])
  
file = open(sys.argv[1], 'r')
T = int(file.readline())
for i in xrange(1, T+1):
  N = int(file.readline())
  L = map(int, file.readline().split(' '))
  P = map(int, file.readline().split(' '))

  assert N == len(L)
  assert N == len(P)

  levels = zip(L, P, range(N))
  levels.sort(lambda li, pi: li[0] * pi[1] - li[1] * pi[0])
  print "Case #%d:" % i, ' '.join([str(i) for li, pi, i in levels])
file.close()
