import itertools, sys

if len(sys.argv) < 2:
  sys.exit('Usage: %s file.in' % sys.argv[0])

def solve(arr):
  sums = dict()
  for i in xrange(len(arr)):
    for subset in itertools.combinations(S, i):
      subset_sum = sum(subset)
      if subset_sum in sums:
        return " ".join([str(j) for j in subset]) + "\n" + " ".join([str(j) for j in sums[subset_sum]])
      else:
        sums[subset_sum] = subset
  return "Impossible"
  
file = open(sys.argv[1], 'r')
T = int(file.readline())
for i in xrange(1, T+1):
  S = sorted(map(int, file.readline().split())[1:])
  print "Case #%d:\n" % i, solve(S)
file.close()
