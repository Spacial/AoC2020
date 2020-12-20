#!/usr/bin/env python3
# License: GPL3
# Day 15

import sys


def part1(data, location):
    numbers = [int(x) for x in data]
    print(numbers)
    rounds = len(numbers)
    lastspoken = {}
    for i in range(rounds):
        lastspoken[numbers[i]] = i
    rounds -= 1
    while rounds < location:
        n = numbers[rounds]
        if numbers[rounds] in lastspoken:
            numbers.append(rounds - lastspoken[n])
            lastspoken[n] = rounds
        else:
            lastspoken[n] = rounds
            numbers.append(0)
        rounds += 1
    return numbers[rounds - 1]


def part2():
    return


entries = []
for line in sys.stdin:
    entries.append(line.strip().split(','))

for e in entries:
    # print(part1(e, 2020))
    print(part1(e, 30000000))
