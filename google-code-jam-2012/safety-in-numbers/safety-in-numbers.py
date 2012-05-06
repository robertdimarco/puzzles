from __future__ import division
import sys

if len(sys.argv) < 2:
  sys.exit('Usage: %s file.in' % sys.argv[0])
  
file = open(sys.argv[1], 'r')
T = int(file.readline())
for i in xrange(1, T+1):
  line = map(int, file.readline().split())
  N, s = line[0], line[1:]
  assert N == len(s)
  X = sum(s)

  # determine minimum total score to prevent elimination
  min_score = 2 * X / N

  # filter contestants already meeting requirements
  scores = [score for score in s if score < min_score]

  # recalculate minimum total score based on filtered list
  min_score = (sum(scores) + X) / len(scores)

  # for each score, determine required audience votes
  votes = [max(0, min_score - score) for score in s]
  M = sum(votes)

  # compute required audience votes as a percentage of total
  m = [100 * vote_count / M for vote_count in votes]

  assert 100 - sum(m) < 0.00001

  print "Case #%d:" % i, ' '.join(map(str, m))  
file.close()
