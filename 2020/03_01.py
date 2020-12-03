"""
Day 3
"""

from utils import read_input


def traverse(grid, x, y):
    loc = [0, 0]
    hits = 0

    while loc[1] < len(grid):
        if grid[loc[1]][loc[0]] == "#":
            hits += 1

        # move
        loc = [loc[0] + x, loc[1] + y]

        if loc[0] >= len(grid[0]):
            loc[0] = loc[0] - len(grid[0])

    return hits


test_input = read_input(3, file_template="{:02}_test")

assert traverse(test_input, 3, 1) == 7

inpt = read_input(3)

assert traverse(inpt, 3, 1) == 257
