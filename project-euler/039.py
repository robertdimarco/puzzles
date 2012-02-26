# coding=utf-8

'''
Problem 39
14 March 2003

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

import euler
best = 120
triples = {}
for n in range(1, 999):
  for m in range(n, 23):
    p = m*(m+n)
    k = 1
    while (p*k < 1001):
      a = k*(m**2 - n**2)
      b = k*(2*m*n)
      c = k*(m**2 + n**2)
      if euler.is_pythagorean_triple(a, b, c):
        if (p*k in triples):
          triples[p*k][(a,b,c)] = True
        else:
          triples[p*k] = {(a,b,c): True}
        if (best not in triples) or (len(triples[p*k]) > len(triples[best])):
          best = p*k
      k += 1
print best
