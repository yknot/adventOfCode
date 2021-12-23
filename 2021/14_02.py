"""
Day 14, part 2
"""
from collections import defaultdict
from utils import read_input


def make_polymer(inpt, itrs):
    start = {a + b: 1 for a, b in zip(inpt[0][:-1], inpt[0][1:])}

    mapping = {a: b for a, b in inpt[2:]}

    for _ in range(itrs):
        new_start = defaultdict(int)
        for k, v in start.items():
            mid = mapping[k]
            new_start[k[0] + mid] += v
            new_start[mid + k[1]] += v

        start = new_start

    counts = defaultdict(int)
    for k, v in start.items():
        counts[k[0]] += v

    counts[inpt[0][-1]] += 1
    max_val = max(counts.values())
    min_val = min(counts.values())

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
assert make_polymer(test_inpt, 10) == 1588
assert make_polymer(test_inpt, 40) == 2188189693529


inpt = list(read_input(14, line_parser=parser))
assert make_polymer(inpt, 40) == 2884513602164
