#!/usr/bin/env python3
# License: GPL3
# Day 14

import sys


def cleanData(data):
    cleaned = {}
    reading = False
    # print(data)
    for i in range(len(data)):
        line = data[i].split('=')
        # print(line, reading)
        if line[0][:3] == 'mas':
            if reading:
                cleaned[len(cleaned)+1] = {mask: mem}
                reading = False
            else:
                mask = line[1]
                mem = []
                reading = True
            # print('mask')
        elif line[0][:3] == 'mem':
                loc = line[0].split(']')[0]
                value = int(line[1])
                mem.append((int(loc[4:]), value))
    cleaned[len(cleaned)] = {mask: mem}
    return cleaned


def part1(data):
    for k, v in data.items():
        print('working on:', k)
        for mask, mem in v.items():
            print(mask, mem)
    return


def part2():
    return


entries = []
for line in sys.stdin:
    entries.append(line.strip())

print(part1(cleanData(entries)))
