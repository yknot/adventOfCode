"""
Day 1 part 2
"""
from utils import read_input
from itertools import combinations


def find_2020(vals):
    for x, y, z in combinations(vals, 3):
        if x != y and x != z and y != z and x + y + z == 2020:
            return x * y * z

    return -1


inpt = list(read_input(1, line_parser=lambda x: int(x)))


assert find_2020(inpt) == 76110336
