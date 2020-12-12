#!/usr/bin/env python3
# License: GPL3
# Day 9

import sys


def valida(lista, start):
    last = lista[-1]
    count = 0
    mark = ['.' for x in range(0, len(lista))]
    for k in range(0, len(lista) - 1):
        for z in range(k + 1, len(lista)):
            soma = lista[k] + lista[z]
            if soma == last:
                count += 1
    if count > 0:
        return True
    else:
        return False


def part1(data, window):
    preamble = []
    for i in range(window + 1, len(data) - 1):
        if not valida(data[i - window - 1: i], i):
            return data[i - 1], (i - 1)


def find(data, n):
    for i in range(0, len(data)):
        for k in range(i + 1, len(data)):
            if (sum(data[i:k])) == n:
                print(data[i:k])
                return i, k


def part2(data, window):
    invalidNumber, idx = part1(data, window)
    mn, mx = find(data[0: idx], invalidNumber)
    minNumber = min(data[mn:mx])
    maxNumber = max(data[mn:mx])
    return minNumber + maxNumber


entries = []
for line in sys.stdin:
    entries.append(int(line.strip()))

# print(part1(entries, 5))
print(part2(entries, 25))
