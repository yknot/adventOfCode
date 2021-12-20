"""
Day 11, part 2
"""
from utils import read_input


def increment_board(board):
    found = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += 1
            if board[i][j] > 9:
                found.append((i, j))

    return board, found


def reset_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 9:
                board[i][j] = 0
    return board


def check_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                return False
    return True


def count_flashes(board):
    itr = 0
    while True:
        itr += 1
        board, found = increment_board(board)

        for i, j in found:
            # increment up
            if i > 0:
                board[i - 1][j] += 1
                if board[i - 1][j] == 10:
                    found.append((i - 1, j))
                # increment up left
                if j > 0:
                    board[i - 1][j - 1] += 1
                    if board[i - 1][j - 1] == 10:
                        found.append((i - 1, j - 1))
                # increment up right
                if j < (len(board[i]) - 1):
                    board[i - 1][j + 1] += 1
                    if board[i - 1][j + 1] == 10:
                        found.append((i - 1, j + 1))
            # increment left
            if j > 0:
                board[i][j - 1] += 1
                if board[i][j - 1] == 10:
                    found.append((i, j - 1))
            # increment right
            if j < (len(board[i]) - 1):
                board[i][j + 1] += 1
                if board[i][j + 1] == 10:
                    found.append((i, j + 1))

            # increment down
            if i < (len(board) - 1):
                board[i + 1][j] += 1
                if board[i + 1][j] == 10:
                    found.append((i + 1, j))
                # increment up left
                if j > 0:
                    board[i + 1][j - 1] += 1
                    if board[i + 1][j - 1] == 10:
                        found.append((i + 1, j - 1))
                # increment up right
                if j < (len(board[i]) - 1):
                    board[i + 1][j + 1] += 1
                    if board[i + 1][j + 1] == 10:
                        found.append((i + 1, j + 1))

        board = reset_board(board)
        if check_board(board):
            return itr


def parser(inpt):
    return [int(i) for i in list(inpt.strip())]


test_inpt = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

test_inpt = [parser(line) for line in test_inpt.split()]
assert count_flashes(test_inpt) == 195

inpt = list(read_input(11, line_parser=parser))
assert count_flashes(inpt) == 312
