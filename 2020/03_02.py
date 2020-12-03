"""
Day 3 part 2
"""

from utils import read_input
from operator import mul


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


def product(lst):
    res = 1
    for l in lst:
        res *= l
    return res


test_input = read_input(3, file_template="{:02}_test")

assert (
    product(
        [
            traverse(test_input, 1, 1),
            traverse(test_input, 3, 1),
            traverse(test_input, 5, 1),
            traverse(test_input, 7, 1),
            traverse(test_input, 1, 2),
        ]
    )
    == 336
)

inpt = read_input(3)

assert (
    product(
        [
            traverse(inpt, 1, 1),
            traverse(inpt, 3, 1),
            traverse(inpt, 5, 1),
            traverse(inpt, 7, 1),
            traverse(inpt, 1, 2),
        ]
    )
) == 1744787392
