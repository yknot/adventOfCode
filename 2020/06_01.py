"""
Day 6 part 1
"""

from utils import read_input


def parse_questions(lines):
    total = 0
    current = set()
    for line in lines:
        if line == "":
            total += len(current)
            current = set()
        else:
            current = current.union(set(line))

    return total + len(current)


test_inpt = ("abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b")
assert parse_questions(test_inpt) == 11

inpt = read_input(6)

assert parse_questions(inpt) == 6782
