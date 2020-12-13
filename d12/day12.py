#!/usr/bin/env python3
# License: GPL3
# Day 12

import sys
import numpy as np


def rotate(pointer, cmd, grads):
    rose = {90:  "A",  # 90/N,
            270: "v",  # 270/S,
            180: "<",  # 180/W,
            0:   ">"}  # 0/E
    # print('  R:', pointer, cmd, grads, end='')
    if cmd == 'R':
        p = (pointer - grads) % 360
    else:
        p = (pointer + grads) % 360
    return p, rose[p]


def updater(cmd, x, y, value):
    # print('  U:', cmd, (x, y), value, end='')
    if cmd == 'N':
        # print("Nor")
        x += value
    elif cmd == 'S':
        x -= value
    elif cmd == 'W':
        y -= value
    elif cmd == 'E':
        y += value
    return x, y


def goForward(pointer, x, y, value):
    # print('  F:', pointer, (x, y), value, end='')
    if pointer == 0:
        # print(" .")
        y += value
    elif pointer == 90:
        # print("x")
        x += value
    elif pointer == 180:
        # print("a")
        y -= value
    elif pointer == 270:
        # print("e")
        x -= value
    return x, y


def part1(data):
    x, y = 0, 0
    pointer = 0
    point = '>'
    # print(data)
    coords = ['N', 'S', 'W', 'E']
    rots = ['R', 'L']
    for i in data:
        cmd, value = i[:1], int(i[1:])
        print(i, cmd, point, value, (x, y), pointer, ' ')
        if cmd in ['F']:
            x, y = goForward(pointer, x, y, value)
        elif cmd in coords:
            x, y = updater(cmd, x, y, value)
        elif cmd in rots:
            pointer, point = rotate(pointer, cmd, value)
        # print('')
        last = i
    print('Final:', last[:1], point, last[1:], x, y, pointer, ' ')
    return abs(x) + abs(y)


def getR(x, y, angle):
    # get angle
    theta = np.radians(angle)
    # print('  A:', angle, (x, y), theta, end='')
    # get rotation matrix
    r = np.array(((np.cos(theta), -np.sin(theta)),
                  (np.sin(theta), np.cos(theta))))
    new = r.dot(np.array((x, y)))
    return new[0], new[1]


def rotwp(pointer, cmd, value, xc, yc):
    rose = {90:  "A",  # 90/N,
            270: "v",  # 270/S,
            180: "<",  # 180/W,
            0:   ">"}  # 0/E
    # print('  R:', pointer, cmd, value, (xc, yc))
    if cmd == 'R':
        flip = -1
    else:
        flip = 1
    nx, ny = getR(xc, yc, flip * value)
    p = (pointer + (flip * value)) % 360
    return round(nx, 0), round(ny, 0), p, rose[p]


def upwp(cmd, xc, yc, value):
    # print('  U:', cmd, (xc, yc), value, end='')
    if cmd == 'N':
        # print("Nor")
        yc += value
    elif cmd == 'S':
        yc -= value
    elif cmd == 'W':
        xc -= value
    elif cmd == 'E':
        xc += value
    return xc, yc


def goFor(pointer, x, y, value, xc, yc):
    # print('  F:', pointer, (x, y), value, (xc, yc), end='')
    if pointer == 0:
        y = y + (yc * value)
    elif pointer == 90:
        x = x + (xc * value)
    elif pointer == 180:
        y = y - (yc * value)
    elif pointer == 270:
        x = x - (xc * value)
    return x, y


def part2(data):
    x, y = 0, 0
    xc, yc = 10, 1
    pointer = 0
    point = '>'
    # print(data)
    coords = ['N', 'S', 'W', 'E']
    rots = ['R', 'L']
    for i in data:
        cmd, value = i[:1], int(i[1:])
        # print(i, cmd, point, value, (x, y), pointer, (xc, yc), ' ')
        if cmd in ['F']:
            # x, y = goFor(pointer, x, y, value, xc, yc)
            # print('  F:', pointer, (x, y), value, (xc, yc), end='')
            x = x + (xc * value)
            y = y + (yc * value)
        elif cmd in coords:
            # print('  WP -> from:', (xc, yc), end='')
            xc, yc = upwp(cmd, xc, yc, value)
            # print('  to:', (xc, yc), end='')
        elif cmd in rots:
            xc, yc, pointer, point = rotwp(pointer, cmd, value, xc, yc)
        # print('')
        last = i
    # print('Final2:', last[:1], point, last[1:], x, y, pointer, ' ')
    return int(abs(x) + abs(y))


entries = []
for line in sys.stdin:
    entries.append(line.strip())

# print(part1(entries))
print(part2(entries))
