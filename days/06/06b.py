#!/usr/bin/env python3

import numpy as np

from aoc import get_inputs

lines = get_inputs(6, False)

fishes = np.array(list(map(int, lines[0].split(","))), dtype=np.byte)

fishes_by_age = np.zeros(9, dtype=int)
for i in range(9):
    fishes_by_age[i] = len(fishes[fishes == i])

for i in range(256):
    new_fishes = fishes_by_age[0]
    fishes_by_age = np.roll(fishes_by_age, -1)
    fishes_by_age[6] += new_fishes

print(sum(fishes_by_age))
