import sys

if len(sys.argv) < 2:
  sys.exit('Usage: %s file.in' % sys.argv[0])

file = open(sys.argv[1], 'r')
T = int(file.readline())
for i in xrange(T):
  A, B = map(int, file.readline().split())
  p = map(float, file.readline().split())
  pj, optimal = 1, B + 2
  for j in xrange(A):
    pj *= p[j]
    optimal = min(optimal, A + (2 * (B - j)) - (pj * (B+1)))
  print 'Case #%d: %f' % (i+1, optimal)
file.close()
