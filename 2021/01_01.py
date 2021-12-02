"""
Day 1
"""
from utils import read_input


test_inpt = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def find_increases(vals):
    prev = vals[0]
    increases = 0
    for i in vals[1:]:
        if i > prev:
            increases += 1
        prev = i

    return increases


inpt = list(read_input(1, line_parser=lambda x: int(x)))

assert find_increases(test_inpt) == 7

assert find_increases(inpt) == 1316
