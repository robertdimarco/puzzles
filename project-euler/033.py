# coding=utf-8

'''
Problem 33
20 December 2002

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

from __future__ import division
import fractions
answer = 1
for i in range(10,100):
  for j in range(i, 100):
    if (i != j) and (int(j%10) != 0) and (int(i%10) == int(j/10)) and ((i/j) == (int(i/10)/int(j%10))):
      answer *= (i / j)
print fractions.Fraction(str(answer))
