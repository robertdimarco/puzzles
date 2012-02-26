# coding=utf-8

'''
Problem 42
25 April 2003

The n^(th) term of the sequence of triangle numbers is given by, t_(n) = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using 042.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

import string
file = open('042.txt', 'r')
x, triangle_numbers = 0, {}
for i in range(10**3):
  x += i
  triangle_numbers[x] = True
def score(index):
  return sum(ord(i)-64 for i in names[index-1])
names = string.replace(file.read(), '"', '').split(',')
print sum(1 for i in range(len(names)+1) if score(i) in triangle_numbers)
