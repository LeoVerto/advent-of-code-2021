#!/usr/bin/env python3
from aoc import get_inputs

lines = get_inputs(1)

count = 0
prev = [9999, 9999, 9999]

for a in lines:
    if sum([prev[1], prev[2], a]) > sum(prev):
        count += 1
    prev = [prev[1], prev[2], a]

print(count)
