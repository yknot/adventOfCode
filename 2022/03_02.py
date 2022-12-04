"""
Day 3
"""
from utils import read_input


test_inpt = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def compute_score(vals):
    total = 0
    i = 0
    while i < len(vals):
        v = list(
            set(vals[i]).intersection(set(vals[i + 1])).intersection(set(vals[i + 2]))
        )[0]
        if v.isupper():
            total += ord(v) - 38
        else:
            total += ord(v) - 96

        i += 3

    return total


inpt = list(read_input(3))

assert compute_score(test_inpt.split("\n")) == 70

assert compute_score(inpt) == 2668
