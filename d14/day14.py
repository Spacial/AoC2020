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
    memall = {}
    for k, v in data.items():
        print('working on:', k)
        for mask, mem in v.items():
            # print(mask, mem)
            # currmask = int(''.join([mask[x] if mask[x] != 'X' else '0' for x in range(1, len(mask))]), 2)
            currmask = mask.strip()
            # print(''.join(currmask), len(mask))
            print(currmask)
            # print(mask)
            for m in mem:
                addr, value = m
                print(addr, value)
                getpadbin = lambda x, n: format(x, 'b').zfill(n)

                binval = getpadbin(value, len(currmask))
                maskedvalue = [0 for x in currmask]

                for i in range(0, len(currmask)):
                    if currmask[i] == 'X':
                        maskedvalue[i] = binval[i]
                    else:
                        maskedvalue[i] = currmask[i]
                print(binval)
                print(currmask)
                # print(maskedvalue)
                # print(len(maskedvalue))
                print(''.join(maskedvalue))
                intnewval = int(''.join(maskedvalue), 2)
                if intnewval != 0:
                    memall[addr] = intnewval
                # memall[addr] = value and currmask
    print(memall)
    sum = 0
    for i in memall:
        sum += memall[i]
    return sum


def part2():
    return


entries = []
for line in sys.stdin:
    entries.append(line.strip())

print(part1(cleanData(entries)))
