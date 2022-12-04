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
    for line in vals:
        half = len(line) // 2
        v = list(set(line[:half]).intersection(set(line[half:])))[0]
        if v.isupper():
            total += ord(v) - 38
        else:
            total += ord(v) - 96

    return total


inpt = list(read_input(3))

assert compute_score(test_inpt.split("\n")) == 157

assert compute_score(inpt) == 8139
