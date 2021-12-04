#!/usr/bin/env python3

import numpy as np

from aoc import get_inputs

lines = get_inputs(4, False)

draws = lines[0].split(",")

board_list = []
for i in range(2, len(lines), 6):
    board_list.append(list(map(lambda x: x.split(), lines[i:i+5])))

boards = np.array(board_list, dtype=np.byte)
boards += 1

keep = list(range(0, boards.shape[0]))

for draw in draws:
    draw = int(draw) + 1
    for i in range(len(boards)):
        if i not in keep:
            continue

        board = boards[i]
        board[board == draw] = 0

        if 0 in np.sum(board, axis=0) or 0 in np.sum(board, axis=1):
            keep.remove(i)

            if len(keep) == 0:
                boards[i][board > 0] -= 1
                print(np.sum(boards[i]) * (draw - 1))
                exit(0)
