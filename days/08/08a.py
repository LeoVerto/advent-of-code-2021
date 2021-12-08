#!/usr/bin/env python3

import numpy as np

from aoc import get_inputs

lines = get_inputs(8, False)

counts = np.zeros(10, dtype=int)

for line in lines:
    inputs = line.split(" ")[:9]
    outputs = line.split(" ")[11:]

    for o in outputs:
        if len(o) == 2:
            counts[1] += 1
        elif len(o) == 3:
            counts[7] += 1
        elif len(o) == 4:
            counts[4] += 1
        elif len(o) == 7:
            counts[8] += 1

print(sum(counts))
