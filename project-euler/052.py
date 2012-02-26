# coding=utf-8

'''
Problem 52
12 September 2003

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

import euler
for i in range(1, 10**6):
  valid = True
  for j in range(2, 7):
    if not euler.is_permutation(i, i*j):
      valid = False
      break
  if (valid):
    print i
    break
