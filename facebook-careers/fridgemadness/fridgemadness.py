#!/usr/bin/env python

import sys

def computePrefLevel(a, b):
    sum = 0
    n = len(a)
    for i in range(0, n):
        if (a[i] == b[i]): sum += (n-i)*(n-i)
        else: sum += (n-i)
        for j in range(0,i):
            if (b[j] == a[i]): sum -= (n-i)
    return sum

def stableMarriage(filename):
    f = open(filename, 'r')
    line = f.readline()
    m,n = (int)(line.split()[0]),(int)(line.split()[1])
    inputPrefs = []
    prefsA = []
    prefsB = []
    for i in range(0, n): f.readline()
    for i in range(0, m): inputPrefs.append(f.readline().strip().split()[1].split(','))
    for i in range(0, m/2):
        rank = []
        for j in range(m/2,m):
            rank.append(computePrefLevel(inputPrefs[i],inputPrefs[j]))
        prefsA.append(list(index for index, item in sorted(enumerate(rank), key=lambda x: (x[1],x[0]),reverse=True)))
    for i in range(m/2, m):
        rank = []
        for j in range(0,m/2):
            rank.append(computePrefLevel(inputPrefs[i],inputPrefs[j]))
        prefsB.append(list(index for index, item in sorted(enumerate(rank), key=lambda x: (x[1],x[0]),reverse=True)))
    paired = [-1]*m
    unpairedA = range(0,m/2)
    while (len(unpairedA) > 0):
        a = unpairedA[0]
        unpairedA.remove(a)
        for i in range(0, m/2):
            b = prefsA[a][i]
            c = b + m/2
            if (paired[c] == -1):
                paired[a] = c
                paired[c] = a
                break
            else:
                if (prefsB[b].index(a) < prefsB[b].index(paired[c])):
                    unpairedA.append(paired[c])
                    paired[paired[c]] = -1
                    paired[a] = c
                    paired[c] = a
                    break
    for i in range(0, m/2):
        print i, paired[i]
                

if (len(sys.argv) == 2):
	stableMarriage(sys.argv[1])
else:
    print "usage: ./fridgemadness <in>"
