#!/usr/bin/env python3

with open("01.txt", "r") as file:
    lines = list(map(int, file))

count = 0
b = 9999

for a in lines:
    if a > b:
        count += 1
    b = a

print(count)
