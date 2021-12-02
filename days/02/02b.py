#!/usr/bin/env python3
from aoc import get_inputs

lines = get_inputs(2, False)

depth = 0
pos = 0
aim = 0

for a in lines:
    args = a.split(" ")
    dist = int(args[1])
    if args[0] == "forward":
        pos += dist
        depth += aim * dist
    elif args[0] == "up":
        aim -= dist
    elif args[0] == "down":
        aim += dist

print(depth * pos)
