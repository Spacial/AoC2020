#!/usr/bin/env python3
# License: GPL3
# Day 14

import sys


def cleanData(data):
    cleaned = {}
    masks = []
    for i in range(len(data)):
        line = data[i].split('=')
        if line[0][:3] == 'mas':
            masks.append(line[1].strip())
    midx = 0
    mem = []
    start = True
    for i in range(len(data)):
        line = data[i].split('=')
        if line[0][:3] == 'mem':
            loc = line[0].split(']')[0]
            value = int(line[1])
            mem.append((int(loc[4:]), value))
        else:
            if start:
                start = False
            else:
                cleaned[len(cleaned)] = {masks[midx]: mem}
                midx += 1
                mem = []
    cleaned[len(cleaned)] = {masks[midx]: mem}
    return cleaned


def part1(data):
    allmem = {}
    for k, v in data.items():
        for mask, mem in v.items():
            for addr, value in mem:
                sbvalue = [s for s in '{0:0b}'.format(value).zfill(len(mask))]
                listmask = [m for m in mask]
                newvalue = []
                for b in range(len(sbvalue)):
                    if listmask[b] == 'X':
                        newvalue.append(sbvalue[b])
                    else:
                        newvalue.append(mask[b])
                binint = int(''.join(newvalue), 2)
                allmem[addr] = binint
    s = 0
    for a, v in allmem.items():
        s += v
    return s


def floatingBit(mask, value, start):
    if len(mask) == start:
        return []
    thisflips = []
    for m in range(start, mask):
        if mask[m] == 'X':
            flipz = value.copy()
            flipo = value.copy()
            flipz[m] = 0
            flipo[m] = 1
            thisflips.append(floatingBit(mask, flipz, m))
            thisflips.append(floatingBit(mask, flipo, m))
    return thisflips


def part2(data):
    allmem = {}
    for k, v in data.items():
        for mask, mem in v.items():
            for addr, value in mem:
                sbvalue = [s for s in '{0:0b}'.format(value).zfill(len(mask))]
                listmask = [m for m in mask]
                newvalue = []
                for b in range(len(sbvalue)):
                    if listmask[b] == 'X':
                        newvalue.append(sbvalue[b])
                    else:
                        newvalue.append(mask[b])
                binint = int(''.join(newvalue), 2)
                allmem[addr] = binint
    s = 0
    for a, v in allmem.items():
        s += v
    return s


entries = []
for line in sys.stdin:
    entries.append(line.strip())

# print(part1(cleanData(entries)))
print(part2(cleanData(entries)))
