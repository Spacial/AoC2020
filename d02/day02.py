#!/usr/bin/env python3
# License: GPL3
# Day 02

import sys

def valids1(policy, password):
    minchar=int(policy.split(' ')[0].split('-')[0].strip())
    maxchar=int(policy.split(' ')[0].split('-')[1].strip())
    charac=policy.split(' ')[1].strip()
    countchar = 0
    for i in range(0, len(password)):
        if password[i] == charac:
            countchar += 1
            if countchar > maxchar:
                return False
    if countchar >= minchar:
        return True
    return False

def valids2(policy, password):
    fstchar=int(policy.split(' ')[0].split('-')[0].strip())
    scnchar=int(policy.split(' ')[0].split('-')[1].strip())
    charac=policy.split(' ')[1].strip()
    one = two = False
    if password[fstchar] == charac:
        one = True
    if password[scnchar] == charac:
        two = True
    return one ^ two

def call(entries):
    valids = 0
    for e in entries:
        policy, password = e.split(':')
        if valids2(policy, password):
            valids += 1
    print(valids)

entries = []
for line in sys.stdin:
    entries.append(line.strip())

call(entries)