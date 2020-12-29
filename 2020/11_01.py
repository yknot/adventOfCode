"""
Day 11 part 1

"""

import copy
from utils import read_input


def step(board):
    new_board = copy.deepcopy(board)
    n_board = len(board)
    n_line = len(board[0])
    for i, line in enumerate(board):
        for j, l in enumerate(line):
            if board[i][j] == ".":
                continue
            to_eval = []
            if i > 0:
                if j > 0 and j + 1 < n_line:
                    to_eval += board[i - 1][j - 1 : j + 2]
                elif j > 0:
                    to_eval += board[i - 1][j - 1 :]
                elif j + 1 < len(line):
                    to_eval += board[i - 1][: j + 2]

            if i + 1 < n_board:
                if j > 0 and j + 1 < n_line:
                    to_eval += board[i + 1][j - 1 : j + 2]
                elif j > 0:
                    to_eval += board[i + 1][j - 1 :]
                elif j + 1 < n_line:
                    to_eval += board[i + 1][: j + 2]

            if j > 0:
                to_eval.append(board[i][j - 1])
            if j + 1 < n_line:
                to_eval.append(board[i][j + 1])

            if board[i][j] == "#" and to_eval.count("#") >= 4:
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

assert run_grid(test_inpt) == 37

inpt = read_input(11)

assert run_grid(inpt) == 2359
