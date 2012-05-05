import math

# Level 1

def longest_palindrome_substring(string):
  strlen, best, pos = len(string), 0, 0
  for i in range(1, strlen):
    for lower, upper, curlen in [(i - 1, i + 1, 1), (i, i + 1, 0)]:
      while lower >= 0 and upper < strlen and string[lower] == string[upper]:
        lower, upper, curlen = lower - 1, upper + 1, curlen + 2
      if (curlen > best):
        best, pos = curlen, lower + 1
  return string[pos:pos + best]

assert "racecar" == longest_palindrome_substring("I like racecars that go fast")

file = open('gettysburg.txt')
print longest_palindrome_substring(file.read())
file.close()

# Level 2

def gen_fibonacci():
  a, b = 0, 1
  while True:
    yield a
    b = a + b
    yield b
    a = a + b

def is_prime(n):
  if n <= 1:
    return False
  n = abs(n)
  i = 2
  while i <= math.sqrt(n):
    if n % i == 0:
      return False
    i += 1
  return True

def prime_factors(n):
  i = 2
  while i <= math.sqrt(n):
    if n % i == 0:
      factors = prime_factors(n / i)
      factors.append(int(i))
      return factors
    i += 1
  return [int(n)]

for i in gen_fibonacci():
  if i > 227000 and is_prime(i):
    print sum(set(prime_factors(i + 1)))
    break

# Level 3

def check_subsets(hashmap, arr, n, i, count, total):
  valid = 0
  if count < n-1:
    for j in range(i+1, n):
      valid += check_subsets(hashmap, arr, n, j, count + 1, total + arr[j])
  if count > 1 and total in hashmap:
    valid += 1
  return valid

def num_subset_sums(arr):
  arr, hashmap = sorted(arr), dict.fromkeys(arr, True)
  return check_subsets(hashmap, arr, len(arr), -1, 0, 0)

assert 4 == num_subset_sums([1, 2, 3, 4, 6])

file = open('numbers.csv')
print num_subset_sums(map(int, file.read().split(',')))
file.close()
