# coding=utf-8

'''
Problem 57
21 November 2003

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

  √2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

  1 + 1/2 = 3/2 = 1.5
  1 + 1/(2 + 1/2) = 7/5 = 1.4
  1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
  1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
'''

sum = 0
a1, a0, b1, b0 = 1, 1, 1, 0
for i in range(1000):
  a2, b2 = 2*a1+a0, 2*b1+b0
  a1, a0, b1, b0 = a2, a1, b2, b1
  if (len(str(a2)) > len(str(b1))): sum += 1
print sum
