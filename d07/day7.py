#!/usr/bin/env python3
# License: GPL3
# Day 7
# same ideia: https://github.com/dedolence/AoC-2020-Day07/blob/master/part1.py

import sys


def getBags(entries):
    Bags = {}
    for line in entries:
        halves = line.strip().split("contain")
        bagName = halves[0].replace(' ', '')[:-4]
        bagContents = halves[1].strip().split(', ')
        cDict = {}
        for content in bagContents:
            content = content.strip().replace('.', '')
            if content != "no other bags":
                contentArray = content.strip().split(' ')
                contentQuantity = contentArray[0]
                contentName = contentArray[1] + contentArray[2]
                cDict[contentName] = contentQuantity
        Bags[bagName] = cDict
    # print(Bags)
    return Bags


def parentSearch(allP, parent, bag, Bags):
    children = [c for c in Bags[parent].keys()]
    if children:
        for child in children:
            if child == bag:
                return True
            else:
                if parentSearch(allP, child, bag, Bags):
                    return True
    else:
        return False


def checkBag(bag, Bags):
    allp = []
    for parent in Bags:
        if parentSearch(allp, parent, bag, Bags):
            allp.append(parent)
    return allp


def getChildren(bag, Bags, childrenArray):
    if childrenArray is None:
        childrenArray = []
    children = Bags[bag]
    for child in children:
        n = child
        q = int(children[child])
        for x in range(q):
            childrenArray.append(item for item in getChildren(n, Bags, childrenArray))
    return childrenArray


def part2(entries, bag):
    Bags = getBags(entries)
    childrenArray = getChildren(bag, Bags, None)
    print(len(childrenArray))


def part1(entries, bag):
    Bags = getBags(entries)
    parents = checkBag(bag, Bags)
    print(len(parents))


entries = []
for line in sys.stdin:
    entries.append(line.strip())

# part1(entries, 'shinygold')
part2(entries, 'shinygold')
