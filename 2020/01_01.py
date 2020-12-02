"""
Day 1
"""
from utils import read_input
from itertools import combinations


def find_2020(vals):
    for x, y in combinations(vals, 2):
        if x != y and x + y == 2020:
            return x * y

    return -1


inpt = list(read_input(1, line_parser=lambda x: int(x)))

assert find_2020(inpt) == 889779
