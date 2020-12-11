#!/usr/bin/env python3
# License: GPL3
# Day 6

import sys
from collections import Counter


def common(str1, str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    commonDict = dict1 & dict2
    if len(commonDict) == 0:
        return ''
    commonChars = list(commonDict.elements())
    commonChars = sorted(commonChars)
    return (''.join(commonChars))


def part1(entries):
    sum = 0
    for e in entries:
        s = sorted(set(e.replace('\n', '')))
        sum += len(s)
    return sum


def part2(entries):
    sum = 0
    for e in entries:
        persons = e.split('\n')
        if len(persons) == 1:
            sum += len(persons[0])
        elif len(persons) > 1:
            sames = persons[0]
            for i in range(1, len(persons)):
                tmp = common(sames, persons[i])
                if tmp != '':
                    sames = tmp
                else:
                    sames = ''
                    pass
            sum += len(sames)
    return sum+1


entries = sys.stdin.read().split('\n\n')

print(part1(entries))
print(part2(entries))
