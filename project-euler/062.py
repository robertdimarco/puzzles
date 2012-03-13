# coding=utf-8

'''
Problem 62
30 January 2004

The cube, 41063625 (345^(3)), can be permuted to produce two other cubes: 56623104 (384^(3)) and 66430125 (405^(3)). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

cubes = {}
solution, i = 0, 0
while solution == 0:
  i += 1
  cube = "".join(sorted(list(str(i**3))))
  if cube not in cubes:
    cubes[cube] = [i]
  else:
    cubes[cube] += [i]
    if len(cubes[cube]) == 5:
      solution = min(cubes[cube])**3
print solution
