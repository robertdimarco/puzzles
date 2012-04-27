from __future__ import division
import bs4, math, operator

# Problem 1: Math

def R(n):
  return sum(map(int, str(math.factorial(n))))
  
i = 0
while (R(i) != 8001):
  i += 1
print i

# Problem 2: HTML

def std_dev(arr):
  mean = sum(arr) / len(arr)
  return math.sqrt(sum((i-mean)**2 for i in arr) / len(arr))

def get_depths(root, tag, depth=0, depths=[]):
  if hasattr(root, 'name'):
    if root.name == tag:
      depths.append(depth)
    for child in root.children:
      get_depths(child, tag, depth + 1, depths)
  return depths

file = open('2.html')
doc = bs4.BeautifulSoup(file.read())
article = doc.find('article')
depths = get_depths(article, 'p')
print round(std_dev(depths), 1)

# Problem 3: Zipf's law

freq = [2520/(i) for i in xrange(1, 901)]
i, total, target = 0, 0, sum(freq)/2
while total < target:
  total += freq[i]
  i += 1
print i
