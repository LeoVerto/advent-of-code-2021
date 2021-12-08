#!/usr/bin/env python3

from aoc import get_inputs

lines = get_inputs(8, False)
output_sum = 0


def get_diff(a, b) -> [str]:
    return list(set(a).difference(b))


for line in lines:
    inputs = line.split(" ")[:10]
    outputs = line.split(" ")[11:]

    segmap: dict[str, str] = {}
    digits = [set()] * 10

    for i in inputs:
        if len(i) == 2:
            digits[1] = set(i)
        elif len(i) == 3:
            digits[7] = set(i)
        elif len(i) == 4:
            digits[4] = set(i)
        elif len(i) == 7:
            digits[8] = set(i)

    segmap["a"] = get_diff(digits[7], digits[1])[0]

    # 6, c
    for i in inputs:
        if len(i) == 6:
            if (c := get_diff(digits[8], i)[0]) in digits[1]:
                digits[6] = set(i)
                segmap["c"] = c
                inputs.remove(i)
                break

    # f
    segmap["f"] = digits[1].difference([segmap["c"]]).pop()

    # 5, e
    for i in inputs:
        if len(i) == 5:
            if delta := get_diff(digits[6], i):
                if len(delta) == 1:
                    digits[5] = set(i)
                    segmap["e"] = delta[0]
                    inputs.remove(i)
                    break

    # 9
    digits[9] = digits[8].copy()
    digits[9].remove(segmap["e"])

    inputs = list(filter(lambda x: set(x) not in digits, inputs))

    # 6, d
    for i in inputs:
        if len(i) == 6:
            d = get_diff(digits[8], i)[0]
            digits[0] = set(i)
            segmap["d"] = d
            inputs.remove(i)
            break

    # 3
    for i in inputs:
        if segmap["c"] in i and segmap["f"] in i:
            digits[3] = set(i)
            inputs.remove(i)
            break

    # 2
    digits[2] = set(inputs[0])

    i = 3
    for o in outputs:
        for j in range(len(digits)):
            if set(o) == digits[j]:
                output_sum += j * (10 ** i)
                break
        i -= 1

print(output_sum)
