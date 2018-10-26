"""day 19 part 1"""
import numpy as np


def remove(e):
    """remove every other element and maybe the first"""
    remove_first = True if len(e) % 2 == 1 else False
    mask = np.ones(len(e), np.bool)
    mask[range(1, len(e), 2)] = 0
    e = np.array(e)[mask]
    if remove_first:
        e = e[1:]
    return e


def run_algo(n):
    """run the full algo"""
    elves = list(range(1, n + 1))
    while len(elves) > 1:
        elves = remove(elves)

    return elves[0]


assert run_algo(5) == 3
print(run_algo(3012210))
