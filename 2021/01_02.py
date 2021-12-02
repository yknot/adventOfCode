"""
Day 1 part 2
"""
from utils import read_input


test_inpt = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def find_triple_increases(vals):
    increases = 0
    for i, _ in enumerate(vals[:-3]):
        if sum(vals[i : i + 3]) < sum(vals[i + 1 : i + 4]):
            increases += 1

    return increases


inpt = list(read_input(1, line_parser=lambda x: int(x)))

assert find_triple_increases(test_inpt) == 5

assert find_triple_increases(inpt) == 1344
