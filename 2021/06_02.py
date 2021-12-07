"""
Day 6, part 2
"""
from utils import read_input


def count_lanternfish(inpt, days):
    # setup
    counts = [0] * 9
    for i, _ in enumerate(counts):
        counts[i] = inpt.count(i)

    for _ in range(days):
        next_val = 0
        prev_val = 0
        for i in range(8, 0, -1):
            next_val = counts[i]
            counts[i] = prev_val
            prev_val = next_val

        counts[8] = counts[0]
        counts[6] += counts[0]
        counts[0] = prev_val

    return sum(counts)


def parser(inpt):
    return [int(i) for i in inpt.strip().split(",")]


test_inpt = parser("3,4,3,1,2")
assert count_lanternfish(test_inpt, 256) == 26984457539

inpt = list(read_input(6, line_parser=parser))
assert count_lanternfish(inpt, 256) == 1644286074024
