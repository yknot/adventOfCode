"""
Day 9 part 1
"""

from utils import read_input


def find_missing(vals, pre):

    idx = pre
    while idx < len(vals):

        preamble = set(vals[idx - pre : idx])
        found = False
        for p in preamble:
            if vals[idx] - p in preamble:
                found = True
                break

        if not found:
            return vals[idx]

        idx += 1


test_input = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]

assert find_missing(test_input, 5) == 127

inpt = read_input(9, line_parser=int)

assert find_missing(inpt, 25) == 32321523
