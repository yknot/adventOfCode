"""
Day 14
"""
from utils import read_input


def make_polymer(inpt):
    start = inpt[0]

    mapping = {a: b for a, b in inpt[2:]}

    for _ in range(10):
        new_start = ""
        for a, b in zip(start[:-1], start[1:]):
            mid = mapping[a + b]
            new_start += a
            new_start += mid

        new_start += start[-1]
        start = new_start

    max_val = 0
    min_val = start.count(start[0])
    for l in set(start):
        cnt = start.count(l)
        if cnt > max_val:
            max_val = cnt
        if cnt < min_val:
            min_val = cnt

    return max_val - min_val


def parser(line):
    if "->" in line:
        return line.strip().split(" -> ")
    return line.strip()


test_inpt = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

test_inpt = [parser(line) for line in test_inpt.split("\n")]
assert make_polymer(test_inpt) == 1588


inpt = list(read_input(14, line_parser=parser))
assert make_polymer(inpt) == 2233
