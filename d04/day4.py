#!/usr/bin/env python3
# License: GPL3
# Day 4

import sys
import re


def part1(data):
    requiredfields = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    valids = 0
    for i in data:
        thisfields = 0
        for f in i:
            if f in requiredfields:
                thisfields += 1
        if thisfields == len(requiredfields):
            valids += 1
    return valids


def validateField(field, data):
    hclRegex = "^#[A-Fa-f0-9]{6}"
    p = re.compile(hclRegex)
    byr = [1920, 2002]
    iyr = [2010, 2020]
    eyr = [2020, 2030]
    hgtcm = [150, 193]
    hgtin = [59, 76]
    ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    pid = 9
    if field in ['byr', 'iyr', 'eyr', 'hgt']:
        if field == 'byr':
            if int(data) < byr[0] or int(data) > byr[1]:
                # print('byr:0,', end='')
                return False
        if field == 'iyr':
            if int(data) < iyr[0] or int(data) > iyr[1]:
                # print('iyr:0,', end='')
                return False
        if field == 'eyr':
            if int(data) < eyr[0] or int(data) > eyr[1]:
                # print(field, data, eyr)
                # print('eyr:0,', end='')
                return False
        if field == 'hgt':
            size = data.split('c')[0]
            if len(data.split('c')) > 1:
                if hgtcm[0] <= int(size) <= hgtcm[1]:
                    return True
            size = data.split('i')[0]
            if len(data.split('i')) > 1:
                if hgtin[0] <= int(size) <= hgtin[1]:
                    return True
            return False
    elif field == 'ecl':
        if data not in ecl:
            # print('ecl:0,', end='')
            return False
    elif field == 'hcl':
        if not (re.search(p, data)):
            # print('hcl:0,', end='')
            return False
    elif field == 'pid':
        if len(data) != pid and type(data) != int:
            # print('pid:0,', end='')
            return False
    return True


def part2(data):
    valids = 0
    for person in data:
        thisfields = 0
        for f in person:
            if validateField(f, person[f]):
                thisfields += 1
        if thisfields == len(person):
            valids += 1
    return valids


lst = sys.stdin.read().split('\n\n')
lst = [x.replace('\n', ' ').split() for x in lst]
passports = []
for person in lst:
    passports.append(dict(data.split(':') for data in person))

print(part1(passports))

passports = [x for x in passports if len(x.keys()) == 8 or (len(x) == 7 and 'cid' not in x.keys())]

print(part2(passports))