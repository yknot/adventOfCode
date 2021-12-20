"""
Day 11
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
    tot = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 9:
                board[i][j] = 0
                tot += 1
    return board, tot


def count_flashes(board):
    tot = 0
    for itr in range(100):
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

        board, count = reset_board(board)
        tot += count
    return tot


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
assert count_flashes(test_inpt) == 1656

inpt = list(read_input(11, line_parser=parser))
assert count_flashes(inpt) == 1640
