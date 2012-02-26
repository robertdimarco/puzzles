# coding=utf-8

'''
Problem 41
11 April 2003

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

import euler, itertools
print max(int(''.join(i)) for i in itertools.permutations('1234567') if euler.is_prime(int(''.join(i))))
