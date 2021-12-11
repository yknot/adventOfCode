"""
Day 7
"""
import numpy as np
from utils import read_input


def find_min(crabs):
    med = int(np.median(crabs))
    tot = 0
    for c in crabs:
        tot += abs(c - med)

    return tot


def parser(inpt):
    return [int(i) for i in inpt.strip().split(",")]


test_inpt = parser("16,1,2,0,4,2,7,1,2,14")
assert find_min(test_inpt) == 37

inpt = list(read_input(7, line_parser=parser))
assert find_min(inpt) == 352254
