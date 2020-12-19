"""
Day 9 part 2
"""

from utils import read_input


def find_window(opts, total):

    window = []
    for o in opts:
        window.append(o)
        while sum(window) > total:
            window.pop(0)

        if sum(window) == total:
            return window


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
            window = find_window(vals, vals[idx])
            return min(window) + max(window)

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

assert find_missing(test_input, 5) == 62

inpt = read_input(9, line_parser=int)

assert find_missing(inpt, 25) == 4794981
