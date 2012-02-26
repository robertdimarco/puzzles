# coding=utf-8

'''
Problem 74
16 July 2004

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

  1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

  169 → 363601 → 1454 → 169
  871 → 45361 → 871
  872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

  69 → 363600 → 1454 → 169 → 363601 (→ 1454)
  78 → 45360 → 871 → 45361 (→ 871)
  540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''

import euler
facts = dict(zip(map(str, range(10)), (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)))
chains = {169:3, 363601:3, 1454:3, 871:2, 45361:2, 872:2, 45362:2}
def chain_length(x):
  if x not in chains:
    next = sum(facts[y] for y in str(x))
    chains[x] = 1 if (next == x) else (1 + chain_length(next))
  return chains[x]
print sum(1 for i in xrange(1, 10**6) if chain_length(i) == 60)
