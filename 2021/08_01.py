"""
Day 8
"""
from utils import read_input


def find_unique(inpt):
    tot = 0
    for _, back in inpt:
        for b in back:
            if len(b) in [2, 4, 3, 7]:
                tot += 1

    return tot


def parser(inpt):
    decode, result = inpt.strip().split(" | ")
    return [decode.split(), result.split()]


test_inpt = list(read_input(8, line_parser=parser, file_template="{:02}_test_input"))

assert find_unique(test_inpt) == 26

inpt = list(read_input(8, line_parser=parser))
assert find_unique(inpt) == 321
