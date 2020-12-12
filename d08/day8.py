#!/usr/bin/env python3
# License: GPL3
# Day 8

import sys


def part1(entries):
    unMarked = ['.' for x in range(0, len(entries))]
    acc = 0
    pc = 0
    steps = 0
    while 0 <= pc < len(entries):
        cmd, arg = entries[pc].split(' ')
        if unMarked[pc] != '.':
            return None
        if cmd == 'nop':
            unMarked[pc] = str(steps)
            pc += 1
        elif cmd == 'acc':
            unMarked[pc] = str(steps)
            pc += 1
            acc += int(arg)
        elif cmd == 'jmp':
            unMarked[pc] = str(steps)
            pc += int(arg)
        steps += 1
    return acc


def run(entries, newcmd, i):
    testEntries = entries.copy()
    testEntries[i] = newcmd
    return part1(testEntries)


def part2(entries):
    for i in range(0, len(entries)):
        cmd, arg = entries[i].split(' ')
        r = None
        if cmd == 'nop':
            newcmd = 'jmp ' + arg
            r = run(entries, newcmd, i)
        elif cmd == 'jmp':
            newcmd = 'nop ' + arg
            r = run(entries, newcmd, i)
        if r is not None:
            return r
    return 0


entries = []
for line in sys.stdin:
    entries.append(line.strip())

print(part2(entries))
