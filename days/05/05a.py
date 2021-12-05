#!/usr/bin/env python3

import numpy as np

from aoc import get_inputs

lines = get_inputs(5, False)

vents = list(map(lambda x: tuple(map(int, x.replace(" -> ", ",").split(","))), lines))

field = np.zeros([999, 999], dtype=int)

for vent in vents:
    if not vent[0] == vent[2] and not vent[1] == vent[3]:
        continue
    for x in range(min(vent[0], vent[2]), max(vent[0], vent[2])+1):
        for y in range(min(vent[1], vent[3]), max(vent[1], vent[3])+1):
            field[x][y] += 1

print((field >= 2).sum())
