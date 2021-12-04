#!/usr/bin/env python3

import numpy as np

from aoc import get_inputs

lines = get_inputs(4, False)

draws = lines[0].split(",")

boards = []
for i in range(2, len(lines), 6):
    boards.append(list(map(lambda x: x.split(), lines[i:i+5])))

boards_array = np.array(boards, dtype=np.byte)
boards_array += 1

for draw in draws:
    draw = int(draw) + 1
    for board in boards_array:
        board[board == draw] = 0

        if 0 in np.sum(board, axis=0) or 0 in np.sum(board, axis=1):
            board[board > 0] -= 1
            print(np.sum(board) * (draw - 1))
            exit(0)
