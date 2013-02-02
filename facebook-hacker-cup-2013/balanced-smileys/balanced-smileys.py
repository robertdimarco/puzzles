#!/usr/bin/env python

import re, sys

_globals = {}

def valid():
 return not (re.search('[^a-z:() ]', _globals['str']))

def balanced(start = 0, depth = 0):
  for i in range(start, len(_globals['str'])):
    char = _globals['str'][i];

    if (char == '('):
      depth += 1
    elif (char == ')'):
      depth -= 1
    elif (char == ':') and (i < len(_globals['str']) - 1):
      nextchar = _globals['str'][i+1];
      if (nextchar == '('):
        return balanced(i+2, depth) or balanced(i+2, depth + 1)
      elif (nextchar == ')') and (depth > 0):
        return balanced(i+2, depth) or balanced(i+2, depth - 1)
      elif (nextchar == ')') and (depth <= 0):
        return balanced(i+2, depth)

    if (depth < 0):
      return False

  if (depth == 0):
    return True

t = int(sys.stdin.readline())
for i in range(1, t+1):
  _globals['str'] = sys.stdin.readline().strip()
  result = 'YES' if valid() and balanced() else 'NO'
  print 'Case #%d: %s' % (i, result)