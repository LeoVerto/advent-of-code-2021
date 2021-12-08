#!/usr/bin/env python3

from aoc import get_inputs

lines = get_inputs(8, False)
output_sum = 0


def get_diff(a, b) -> [str]:
    return list(set(a).difference(b))


def find_digit(inputs: [str], digits: [set[str]], length: int, digit: int, other_digit: int, delta_in_digit: int = None) -> str:
    for i in inputs:
        if len(i) == length:
            if delta := get_diff(digits[other_digit], i):
                if len(delta) == 1:
                    if delta_in_digit is None or delta[0] in digits[delta_in_digit]:
                        digits[digit] = set(i)
                        inputs.remove(i)
                        return delta[0]


for line in lines:
    inputs = line.split(" ")[:10]
    outputs = line.split(" ")[11:]

    # maps segment to rewired segment
    segmap: dict[str, str] = {}
    # list of segment sets producing a certain digit
    digits = [set()] * 10

    # 1, 4, 7, 8
    for i in inputs:
        if len(i) == 2:
            digits[1] = set(i)
        elif len(i) == 3:
            digits[7] = set(i)
        elif len(i) == 4:
            digits[4] = set(i)
        elif len(i) == 7:
            digits[8] = set(i)

    # a
    segmap["a"] = get_diff(digits[7], digits[1])[0]

    # 6, c
    segmap["c"] = find_digit(inputs, digits, 6, 6, 8, 1)

    # f
    segmap["f"] = get_diff(digits[1], segmap["c"])[0]

    # 5, e
    segmap["e"] = find_digit(inputs, digits, 5, 5, 6)

    # 9
    digits[9] = digits[8].copy()
    digits[9].remove(segmap["e"])

    # filter already found digits from inputs
    inputs = list(filter(lambda x: set(x) not in digits, inputs))

    # 6, d
    segmap["d"] = find_digit(inputs, digits, 6, 0, 8)

    # 3
    for i in inputs:
        if segmap["c"] in i and segmap["f"] in i:
            digits[3] = set(i)
            inputs.remove(i)
            break

    # 2
    digits[2] = set(inputs[0])

    # calculate output
    i = 3
    for o in outputs:
        for j in range(len(digits)):
            if set(o) == digits[j]:
                output_sum += j * (10 ** i)
                break
        i -= 1

print(output_sum)
