#!/usr/bin/env python3

import numpy as np

from aoc import get_inputs

lines = get_inputs(6, False)

fishes = list(map(int, lines[0].split(",")))

for i in range(256):
    new_fishes = []
    for j in range(len(fishes)):
        fishes[j] -= 1
        if fishes[j] < 0:
            fishes[j] = 6
            new_fishes.append(8)
    fishes += new_fishes

print(len(fishes))
