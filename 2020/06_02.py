"""
Day 6 part 2
"""

from utils import read_input


def parse_questions(lines):
    total = 0
    current = set()
    start = True
    for line in lines:
        if line == "":
            total += len(current)
            current = set()
            start = True
        else:
            if start:
                current = set(line)
                start = False
            else:
                current = current.intersection(set(line))

    return total + len(current)


test_inpt = ("abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b")
assert parse_questions(test_inpt) == 6

inpt = read_input(6)

assert parse_questions(inpt) == 3596
