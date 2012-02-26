# coding=utf-8

'''
Problem 76
13 August 2004

It is possible to write five as a sum in exactly six different ways:

  4 + 1
  3 + 2
  3 + 1 + 1
  2 + 2 + 1
  2 + 1 + 1 + 1
  1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''

def euler076(target, denominations):
  ways = {0:1}
  denominations = sorted(denominations, reverse = True)
  for i in xrange(1,target+1): ways[i] = 0
  for coin in denominations:
    for i in xrange(coin, target+1):
      ways[i] += ways[i-coin]
  return ways[target]
print euler076(100, [i for i in xrange(1,100)])
