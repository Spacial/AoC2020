#!/usr/bin/env python3
# License: GPL3
# Day 10

import sys


def part1(data):
    count = {}
    for j in range(0, 3 + 1):
        count[j] = 0
    s = sorted(data)
    count[s[0] - 0] += 1
    for i in range(0, len(s) - 1):
        if 0 < s[i + 1] - s[i] <= 3:
            count[s[i + 1] - s[i]] += 1
    count[3] += 1
    print(count)
    return count[1] * count[3]


def part2(data):
    last = max(data)
    s = sorted(data)
    index = [1] + [0] * last + [0, 0]
    for i in s:
        index[i] = index[i - 1] + index[i - 2] + index[i - 3]
        if i == last:
            return index[i]


entries = []
for line in sys.stdin:
    entries.append(int(line.strip()))

# print(part1(entries))
print(part2(entries))
