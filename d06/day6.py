#!/usr/bin/env python3
# License: GPL3
# Day 6

import sys


def part1(entries):
    sum = 0
    for e in entries:
        # cleaned = [c.strip() for c in e]
        s = sorted(set(e.replace('\n', '')))
        sum += len(s)
    return sum


# def part2(entries):
#     sum = 0
#     for e in entries:
#         # cleaned = [c.strip() for c in e]
#         persons = e.split('\n')
#         # if pers
#         # for p in persons:
#         if len(persons) == 1:
#             sum += len(persons[0])
#         elif len(persons) > 1:
#             r = set(persons[0])
#             for p in persons:
#                 r = {i for i in r if i in set(p)}
#             print(r)
#         print(len(persons),persons,'-')
#     return sum


entries = sys.stdin.read().split('\n\n')

print(part2(entries))