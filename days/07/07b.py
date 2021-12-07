#!/usr/bin/env python3

import numpy as np

from aoc import get_inputs

lines = get_inputs(7, False)

crabs = np.array(list(map(int, lines[0].split(","))), dtype=int)

avg = np.floor(np.average(crabs))
fuel = np.absolute(crabs - avg)

print(sum(fuel * (fuel + 1) / 2))
