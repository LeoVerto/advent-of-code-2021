#!/usr/bin/env python3
from aoc import get_inputs

lines = get_inputs(1)

count = 0
b = 9999

for a in lines:
    if a > b:
        count += 1
    b = a

print(count)
