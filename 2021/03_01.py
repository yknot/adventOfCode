"""
Day 3
"""
from utils import read_input


test_inpt = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def compute_power(reports):
    sums = len(reports[0]) * [0]
    for report in reports:
        for i, r in enumerate(report):
            sums[i] += int(r)

    mid = len(reports) / 2
    gamma = [int(s > mid) for s in sums]
    epsilon = [0 if g else 1 for g in gamma]

    gamma = "".join([str(g) for g in gamma])
    epsilon = "".join([str(e) for e in epsilon])

    return int(gamma, 2) * int(epsilon, 2)


inpt = list(read_input(3))

assert compute_power(test_inpt) == 198

assert compute_power(inpt) == 3959450
