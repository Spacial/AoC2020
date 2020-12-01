#!/usr/bin/env python3
# License: GPL3
# Day 01

import sys

def part1(entries):
    total=len(entries)
    for n in range(0, total-1):
        for k in range(n, total):
            if entries[n] + entries[k] == 2020:
                print(entries[n]*entries[k])

def part2(entries):
    total=len(entries)
    for n in range(0, total-2):
        for k in range(n, total-1):
            for z in range(k, total):
                if entries[n] + entries[k] + entries[z] == 2020:
                    print(entries[n]*entries[k]*entries[z])


entries = []
for line in sys.stdin:
    entries.append(int(line.strip()))

part2(entries)