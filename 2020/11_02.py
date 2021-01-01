"""
Day 11 part 2

"""

import copy
from utils import read_input

move = {
    "NW": (-1, -1),
    "N": (-1, 0),
    "NE": (-1, +1),
    "W": (0, -1),
    "E": (0, 1),
    "SW": (1, -1),
    "S": (1, 0),
    "SE": (1, 1),
}


def find_dir(brd, x, y, d, x_max, y_max):
    del_x, del_y = move[d]
    x += del_x
    y += del_y
    while True:
        if x < 0 or x >= x_max:
            return "."
        if y < 0 or y >= y_max:
            return "."

        if brd[x][y] == ".":
            x += del_x
            y += del_y
            continue

        return brd[x][y]


def step(board):
    new_board = copy.deepcopy(board)
    n_board = len(board)
    n_line = len(board[0])
    for i, line in enumerate(board):
        for j, l in enumerate(line):
            if board[i][j] == ".":
                continue
            to_eval = []
            for d in ["NW", "N", "NE", "W", "E", "SW", "S", "SE"]:
                to_eval.append(find_dir(board, i, j, d, n_board, n_line))

            if board[i][j] == "#" and to_eval.count("#") >= 5:
                new_board[i][j] = "L"
            elif board[i][j] == "L" and to_eval.count("#") == 0:
                new_board[i][j] = "#"

    return board == new_board, new_board


def run_grid(board):
    board = [list(b) for b in board]

    while True:
        flag, board = step(board)
        if flag:
            break

    return sum([l.count("#") for l in board])


test_inpt = read_input(11, file_template="{:02}_test_input")

assert run_grid(test_inpt) == 26

inpt = read_input(11)

assert run_grid(inpt) == 2131
