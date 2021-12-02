#!/usr/bin/env python3
from aoc import get_inputs

lines = get_inputs(2, False)

depth = 0
pos = 0

for a in lines:
    args = a.split(" ")
    dist = int(args[1])
    if args[0] == "forward":
        pos += dist
    elif args[0] == "up":
        depth -= dist
    elif args[0] == "down":
        depth += dist

print(depth * pos)
