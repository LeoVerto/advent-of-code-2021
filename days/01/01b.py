#!/usr/bin/env python3

with open("01.txt", "r") as file:
    lines = list(map(int, file))

count = 0
prev = [9999, 9999, 9999]

for a in lines:
    if sum([prev[1], prev[2], a]) > sum(prev):
        count += 1
    prev = [prev[1], prev[2], a]

print(count)
