"""
Day 7, part 2
"""
import numpy as np
from utils import read_input


def compute_dist(crabs, med):
    tot = 0
    for c in crabs:
        dist = abs(c - med)
        tot += sum(list(range(1, dist + 1)))
    return tot


def find_min(crabs):
    med = int(np.median(crabs))
    avg = np.mean(crabs)
    move = 1 if avg > med else -1
    avg = int(avg)

    cur = compute_dist(crabs, avg)
    prev = cur + 1
    avg += move

    while prev > cur:
        prev = cur
        cur = compute_dist(crabs, avg)
        avg += move

    return prev


def parser(inpt):
    return [int(i) for i in inpt.strip().split(",")]


test_inpt = parser("16,1,2,0,4,2,7,1,2,14")
assert find_min(test_inpt) == 168

inpt = list(read_input(7, line_parser=parser))
assert find_min(inpt) == 99053143
