#!/usr/bin/env python

import string, sys

m = int(sys.stdin.readline())
for i in range(1, m+1):
  score, line = 0, sys.stdin.readline()
  line = ''.join(char for char in line.lower() if 'a' <= char <= 'z')
  freq = sorted([line.count(char) for char in set(line)])
  for j, num in enumerate(freq):
    score += num * (26 - len(freq) + j + 1)
  print 'Case #%d: %d' % (i, score)