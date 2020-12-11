#!/usr/bin/env python3
# License: GPL3
# Day 5

import sys


def findrow(seat):
    ret = 0
    for i in range(0, len(seat)):
        if seat[len(seat)-i-1] == 'B':
            ret += pow(2, i)
    return ret


def findseat(seat):
    ret = 0
    for i in range(0, len(seat)):
        if seat[len(seat)-i-1] == 'R':
            ret += pow(2, i)
    return ret


def part1(seat):
    return (findrow(seat[:7]) * 8) + findseat(seat[7:])


def part2():
    return

# test cases
# print(part1('FBFBBFFRLR'))
# print(part1('BFFFBBFRRR'))
# print(part1('FFFBBBFRRR'))
# print(part1('BBFFBBFRLL'))

# # part1
# for line in sys.stdin:
#     print(part1(line.strip()))


free = [x for x in range(0, 894)]

for line in sys.stdin:
    occupied = part1(line.strip())
    if occupied in free:
        free.remove(occupied)

print(free)


