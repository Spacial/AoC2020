#!/usr/bin/env python3
# License: GPL3
# Day 3

import sys


def mark(n, c, line):
    lst = list(line)
    lst[n] = c
    return ''.join(lst)


def part1(xslope, yslope, mapa):
    trees = 0
    x = xslope
    for y in range(yslope, len(mapa), yslope):
        x = x % (len(mapa[0]) )
        if mapa[y][x] == '#':
            trees += 1
            mapa[y] = mark(x, 'X', mapa[y])
        else:
            mapa[y] = mark(x, 'O', mapa[y])
        x += xslope
    return trees

entries = []
for line in sys.stdin:
    entries.append(line.strip('\n'))

# print(part1(3, 1, entries))
slopes = [ [1,1], [3,1], [5,1], [7,1], [1,2] ]
k = 1
for i in slopes:
    x, y = i
    ecopy = entries.copy()
    k *= part1(x, y, ecopy)
print(k)
