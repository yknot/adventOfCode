"""
Day 3 part 2
"""
from copy import copy
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


def compute_rating(reports, sort, default):
    idx = 0
    while len(reports) > 1:
        mid = len(reports) / 2
        bin_sum = 0
        reports_ones = []
        reports_zeros = []

        for r in reports:
            bin_sum += int(r[idx])
            if r[idx] == "0":
                reports_zeros.append(r)
            else:
                reports_ones.append(r)

        if bin_sum > mid:
            if sort == "most":
                reports = reports_ones
            elif sort == "least":
                reports = reports_zeros
        elif bin_sum < mid:
            if sort == "most":
                reports = reports_zeros
            elif sort == "least":
                reports = reports_ones
        else:
            if default == 1:
                reports = reports_ones
            elif default == 0:
                reports = reports_zeros

        idx += 1

    return "".join([str(r) for r in reports[0]])


def compute_life_support(reports):

    oxy = compute_rating(copy(reports), "most", 1)
    co2 = compute_rating(copy(reports), "least", 0)
    return int(oxy, 2) * int(co2, 2)


inpt = list(read_input(3))

assert compute_life_support(test_inpt) == 230

assert compute_life_support(inpt) == 7440311
