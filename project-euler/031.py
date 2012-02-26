# coding=utf-8

'''
Problem 31
22 November 2002

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''

target = 200
denominations = sorted([200, 100, 50, 20, 10, 5, 2, 1], reverse = True)
def coins(target, i):
  if (target == 0) or (len(denominations) == (i+1)):
    return 1
  return sum(coins(target - n*denominations[i], i+1) for n in range(0, int(target/denominations[i])+1))
print coins(target, 0)
