#!/usr/bin/env python3
# License: GPL3
# Day 3

import sys


def mark(n, c, line):
    lst = list(line)
    lst[n] = c
    return ''.join(lst)


def mostraMap(mapa):
    for i in mapa:
        print(i)


def multimap(mapa):
    k = (len(mapa) / (len(mapa[0])) ) * 3
    # print("multiplying map by ", k)
    newMap = []
    for i in mapa:
        newline = i*(int(k)+1)
        newMap.append(newline)
    return newMap


def count_trees(yslope, xslope, mapa):
    width = len(mapa[0])
    height = len(mapa)

    pos = [0, 0]
    trees = 0
    while pos[0] < height:
        trees += mapa[pos[0]][pos[1]] == "#"
        pos[1] = (pos[1] + xslope) % width
        pos[0] += yslope

    return trees


def part1(mapa):
    trees = 0
    y = 2
    # novomapa = []
    # novomapa.append(mapa[0])
    # nope = 1
    # init = True
    # print(len(mapa[0]), len(mapa))
    for i in range(1, len(mapa)):
        # log = '   | ' + str(i)+':'+str(y)
        y = y % (len(mapa[0]))
        # try:
        #   log += '='+str(mapa[i][y])
        # except:
        #     print(i)
        #     print(y)
        #     print(mapa[i])
        #     sys.exit(1)
        if mapa[i][y] == '#':
            trees += 1
        #     mapa[i] = mark(y, 'X', mapa[i])
        # else:
        #     mapa[i] = mark(y, 'O', mapa[i])
        #     nope += 1
        # log += '->'+str(mapa[i][y])+'|'+str(y)
        # novomapa.append(mapa[i]+log)
        y += 3
    # mostraMap(novomapa)
    # print('nopes:', nope)
    # print(len(mapa[0]))
    # if trees+nope == len(mapa):
    #     print("ok")
    # else:
    #     print(trees+nope, len(mapa))
    return trees


def part2():
    return


entries = []
for line in sys.stdin:
    entries.append(line.strip('\n'))

print(part1(entries))
print(count_trees(1, 3, entries))
