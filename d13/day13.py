#!/usr/bin/env python3
# License: GPL3
# Day 13

import sys


class color:
    PURPLE = '\033[1;35;48m'
    CYAN = '\033[1;36;48m'
    BOLD = '\033[1;37;48m'
    BLUE = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    BLACK = '\033[1;30;48m'
    UNDERLINE = '\033[4;37;48m'
    END = '\033[1;37;0m'


def printsched(depart, buses):
    maxrest = max([depart % b for b in buses])//2
    halftime = (len(str(depart))//2)
    timetable = ' ' * halftime
    timetable += 'time'
    timetable += ' ' * halftime
    for b in buses:
        bus = ' bus ' + str(b) + '  '
        timetable += bus
    timetable += '\n'
    flag = False
    for i in range(depart - maxrest - 1, depart + maxrest + 1):
        timetable += ' ' * halftime
        newline = ''
        tm = ''
        if i == depart:
            tm += color.YELLOW + str(i) + color.END
            flag = True
        else:
            tm += str(i)
        tm += ' ' * (halftime + 1)
        rest = ' '
        for b in buses:
            bus = (len(' bus ' + str(b) + '  ')//2)-1
            rest += ' ' * bus
            if i % b == 0:
                if flag:
                    rest += color.GREEN + 'D' + color.END
                    flag = False
                    tm = color.GREEN + str(i) + color.END
                    tm += ' ' * (halftime + 1)
                else:
                    rest += 'D'
            else:
                rest += '.'
            rest += ' ' * (bus + 2)
        newline += tm + rest
        timetable += newline + '\n'
    print(timetable)
    return


def part1(data):
    depart = int(data[0])
    buses = [int(x) for x in data[1].split(',') if x != 'x']
    # printsched(depart, buses)
    maxrest = max([depart % b for b in buses])//2
    flag = False
    busid = -1
    waiting = -1
    for i in range(depart - maxrest - 1, depart + maxrest + 1):
        if i == depart:
            flag = True
        for b in buses:
            if i % b == 0:
                if flag:
                    print(i, b)
                    busid = b
                    waiting = (i - depart)
                    return busid * waiting
    # print(busid, waiting)
    return busid * waiting


def part2(data):
    buses = data[1].split(',')
    busesclean = [(int(buses[k]), k) for k in range(len(buses)) if buses[k] != 'x']
    crt = 1
    depart = 0
    for i in range(len(busesclean)-1):
        b = busesclean[i+1][0]
        idx = busesclean[i+1][1]
        crt *= busesclean[i][0]
        # print(b, idx, crt, '   ->  ', end='')
        while (depart + idx) % b != 0:
            depart += crt
        # print(depart, crt)
    # printsched(depart, busesclean)
    return depart


entries = []
for line in sys.stdin:
    entries.append(line.strip())

# print(part1(entries))
print(part2(entries))
