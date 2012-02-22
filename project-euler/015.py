'''
Problem 15
19 April 2002

Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
'''

# Central binomial coefficients are given by C(2n,n) = (2n)!/(n!)^2
# See http://www.research.att.com/~njas/sequences/A000984
import math
print math.factorial(2*20)/((math.factorial(20))**2)
