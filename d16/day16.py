#!/usr/bin/env python3
# License: GPL3
# Day 16

import sys
import numpy as np


def processField(i):
    field = i.split(':')[0]
    interval = i.split(':')[1]
    sp = interval.split(' ')
    # print(sp)
    f = (int(sp[1].split('-')[0]), int(sp[1].split('-')[1]))
    s = (int(sp[3].split('-')[0]), int(sp[3].split('-')[1]))
    return field, f, s


def processData(data):
    cleanedData = {'rest': None, 'ticket': None, 'nearby': None}
    fieldclass = 0
    rest = []
    ticket = {}
    nearby = {}
    line = 0
    for i in data:
        if i == 'your ticket:':
            fieldclass = 1
            continue
        elif i == 'nearby tickets:':
            fieldclass = 2
            continue
        else:
            if fieldclass == 0 and i.strip() != '':
                field, f, s = processField(i)
                rest.append((f, s))
            elif fieldclass == 1 and i.strip() != '':
                ticket = [int(x) for x in i.split(',')]
            elif fieldclass == 2 and i.strip() != '':
                nearby[line] = [int(x) for x in i.split(',')]
        line += 1
    cleanedData['rest'] = rest
    cleanedData['ticket'] = ticket
    cleanedData['nearby'] = nearby
    return cleanedData


def getFields(data):
    fields = {}
    for i in data:
        # print(i)
        if i == 'your ticket:':
            return {'fields': fields}
        else:
            if i.strip() != '':
                field, f, s = processField(i)
                fields[field] = (f, s)
    return None


def validateMinMax(k, mn, mx):
    if mn <= k <= mx:
        return True
    return False


def validateFieldInt(k, fieldint):
    for mi, mx in fieldint:
        if validateMinMax(k, mi, mx):
            return True
    return False


def validateField(k, field):
    for f in field:
        if validateFieldInt(k, f):
            return True
    return False


def outFromLine(ln, rest):
    outliers = []
    for k in ln:
        if not validateField(k, rest):
            outliers.append(k)
    return outliers


def part1(data):
    outliers = []
    for i in data['nearby']:
        outliers += outFromLine(data['nearby'][i], data['rest'])
    return sum(outliers)


def stripOut(ln, rest):
    for k in ln:
        if not validateField(k, rest):
            return False
    return True


def raw2np(data):
    start = 0
    nearby = None
    k = 0
    for i in data:
        if i == 'nearby tickets:':
            start = 1
            nearby = np.zeros((0, len(data[k - 2].split(','))))
        else:
            if i.strip() != '' and start > 0:
                nearby = np.vstack((nearby, [int(x) for x in i.split(',')]))
        k += 1
    return nearby


def preprocess(inpt):
    valids = []
    data = processData(inpt)
    fields = getFields(inpt)
    fmaps = np.zeros((0, len(fields['fields'])))
    adjust = -1
    for i in data['nearby']:
        if adjust < 0:
            adjust = i
        if stripOut(data['nearby'][i], data['rest']):
            valids.append(data['nearby'][i])
            fmaps = np.vstack((fmaps, [x for x in data['nearby'][i]]))
    return fmaps, valids, data, fields


def minimax(fmaps):
    mapped = {}
    for i in range(fmaps.shape[1]):
        mn = min(fmaps[:, i])
        mx = max(fmaps[:, i])
        mapped[i] = {'min': mn,
                     'max': mx}
    return mapped


def getHits(value, f):
    hits = []
    for i in f:
        if validateMinMax(value, f[i][0][0], f[i][0][1]) or validateMinMax(value, f[i][1][0], f[i][1][1]):
            hits.append(i)
    return hits


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def difference(lst1, lst2):
    stripedlist = []
    try:
        if len(lst1) > len(lst2):
            stripedlist = set(lst1).difference(lst2)
        else:
            stripedlist = set(lst2).difference(lst1)
    except TypeError as e:
        print('>', end='')
    return list(stripedlist)


def map2fields(mps, flds):
    colunmsmapped = {}
    for i in range(len(mps)):
        for j in range(len(mps[i])):
            hits = getHits(mps[i][j],  flds)
            colunmsmapped[(i, j)] = hits
    return colunmsmapped


def mappedcols(fmaps, fields):
    fitted = map2fields(fmaps, fields)
    byLen = {}
    cols = {}
    for k in range(0, len(fmaps[0])):
        c = fitted[(0, k)]
        for i in range(1, len(fmaps)):
            n = intersection(c, fitted[(i, k)])
            c = n.copy()
        byLen[k] = len(c)
        cols[k] = c
    by = dict(sorted(byLen.items(), key=lambda item: item[1]))
    return cols, by


def ordDict(by, cols):
    notStarted = True
    for k, v in by.items():
        if notStarted:
            firsts = cols[k].copy()
            notStarted = False
        else:
            takeaway = difference(firsts, cols[k])
            firsts.append(takeaway[0])
            cols[k] = takeaway
    return cols


def part2(inpt):
    fmaps, _, data, fields = preprocess(inpt)
    cols, by = mappedcols(fmaps, fields['fields'])
    lcols = ordDict(by, cols)
    multiplied = 1
    for c, name in lcols.items():
        if name[0].find('departure') >= 0:
            multiplied *= data['ticket'][c]
    return multiplied


entries = []
for line in sys.stdin:
    entries.append(line.strip())

# print(part1(processData(entries)))
print(part2(entries))
