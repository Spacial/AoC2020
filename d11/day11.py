#!/usr/bin/env python3
# License: GPL3
# Day11

import sys
import numpy as np


def ppr(mp):
    if isinstance(mp, np.ndarray):
        for j in range(0, mp.shape[0]):
            s = ''.join([chr(k) for k in mp[j]])
            print(s)
    else:
        for j in range(0, len(mp)):
            s = ''.join([k for k in mp[j]])
            print(s)
    print('-' * len(mp))
    return


def makearray(data):
    x = len(data)
    y = len(data[0])
    m = np.full((x, y), 46)
    for j in range(0, y):
        for i in range(0, x):
            m[i][j] = ord(data[i][j])
    return m


def occupied(data, x, y):
    ocpy = 0
    xmin, xmax, ymin,  ymax = [0, 0, 0, 0]
    if x - 1 < 0:
        xmin = 0
    else:
        xmin = x - 1
    if x + 2 > data.shape[0]:
        xmax = data.shape[0] - 1
    else:
        xmax = x + 1
    if y - 1 < 0:
        ymin = 0
    else:
        ymin = y - 1
    if y + 2 > data.shape[1]:
        ymax = data.shape[1] - 1
    else:
        ymax = y + 1
    tests = 0
    for i in range(xmin, xmax + 1):
        for j in range(ymin, ymax + 1):
            tests += 1
            # ord('#') => 35
            if data[i][j] == 35:
                ocpy += 1
    if tests not in [4, 6, 9]:
        print("O:", [tests, ocpy], [x, y], [xmin, xmax, ymin, ymax])
    if data[x][y] != 35:
        return ocpy
    else:
        return ocpy - 1


def checkMark(data):
    nd = data.copy()
    for i in range(0, data.shape[0]):
        for j in range(0, data.shape[1]):
            ocpy = occupied(data, i, j)
            # ord('L') => 76
            if data[i][j] == 76:
                if ocpy == 0:
                    nd[i][j] = 35
            # ord('#') => 35
            if data[i][j] == 35:
                if ocpy >= 4:
                    nd[i][j] = 76
    return nd


def countOcpy(data):
    ocpy = 0
    for i in range(0, data.shape[0]):
        for j in range(0, data.shape[1]):
            # ord('#') => 35
            if data[i][j] == 35:
                ocpy += 1
    return ocpy


def part1(data):
    matrix = makearray(data)
    last = m = np.full(matrix.shape, 46)
    while not np.array_equal(last, matrix):
        last = matrix.copy()
        matrix = checkMark(last)
    return countOcpy(matrix)


def goDeep(data, x, y, incx, incy):
    i = x + incx
    j = y + incy
    while (0 <= i < data.shape[0] and
           0 <= j < data.shape[1]):
        # ord('#') => 35
        if data[i][j] == 35:
            return 1
        # ord('#') => 76
        elif data[i][j] == 76:
            return 0
        i += incx
        j += incy
    return 0


def deepOcpy(data, x, y):
    clock = [(1, 0),
             (1, 1),
             (0, 1),
             (-1, 1),
             (-1, 0),
             (0, -1),
             (1, -1),
             (-1, -1)]
    ocpy = 0
    for i in clock:
        ocpy += goDeep(data, x, y, i[0], i[1])
    return ocpy


def deepCheck(data):
    nd = data.copy()
    for i in range(0, data.shape[0]):
        for j in range(0, data.shape[1]):
            ocpy = deepOcpy(data, i, j)
            # ord('#') => 76
            if data[i][j] == 76:
                if ocpy == 0:
                    nd[i][j] = 35
            # ord('#') => 35
            if data[i][j] == 35:
                if ocpy >= 5:
                    nd[i][j] = 76
    return nd


def part2(data):
    matrix = makearray(data)
    last = m = np.full(matrix.shape, 46)
    rounds=0
    while not np.array_equal(last, matrix):
        last = matrix.copy()
        matrix = deepCheck(last)
        rounds += 1
    return countOcpy(matrix)


entries = []
for line in sys.stdin:
    entries.append(line.strip())

# print(part1(entries))
print(part2(entries))
