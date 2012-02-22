from __future__ import division

if __name__ == "__main__":
  import importlib, sys, time
  start = time.time()
  importlib.import_module(sys.argv[1])
  finish = time.time()
  print "Time: " + str(round(finish - start, 4)) + "s"
