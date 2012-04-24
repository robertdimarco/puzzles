# coding=utf-8

'''
Problem 67
09 April 2004

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in 067.txt, a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''

tree, sums = [], {}
file = open('067.txt', 'r')
for line in file:
  tree.append(map(int, line.rstrip('\n').split(' ')))

def dfs_max(i=0, j=0):
  if (i >= len(tree) or (j >= len(tree[i]))):
    return 0
  key = str(i) + ':' + str(j)
  if key in sums:
    return sums[key]
  sums[key] = tree[i][j] + max(dfs_max(i+1, j), dfs_max(i+1, j+1))
  return sums[key]

print dfs_max()
