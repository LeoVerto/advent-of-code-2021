#!/usr/bin/env python3

import numpy as np

from aoc import get_inputs

lines = get_inputs(5, False)

vents = list(map(lambda x: tuple(map(int, x.replace(" -> ", ",").split(","))), lines))

field = np.zeros([999, 999], dtype=int)

for vent in vents:
    if vent[0] == vent[2] or vent[1] == vent[3]:
        for x in range(min(vent[0], vent[2]), max(vent[0], vent[2]) + 1):
            for y in range(min(vent[1], vent[3]), max(vent[1], vent[3]) + 1):
                field[x][y] += 1
    else:
        y = vent[1]
        step_x = 1 if vent[0] < vent[2] else - 1
        step_y = 1 if vent[1] < vent[3] else - 1
        for x in range(vent[0], vent[2] + step_x, step_x):
            field[y][x] += 1
            y += step_y

print((field >= 2).sum())
