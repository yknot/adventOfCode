"""
Day 10, part 2
"""
from utils import read_input
import numpy as np

flipped = {"(": ")", "[": "]", "{": "}", "<": ">"}
value = {")": 1, "]": 2, "}": 3, ">": 4}


def fix_incomplete(inpt):
    totals = []
    for line in inpt:
        line_tot = 0
        opening = []
        corrupted = False
        for l in line:
            if l in ["(", "[", "{", "<"]:
                opening.append(l)
            elif l == flipped[opening[-1]]:
                opening.pop(-1)
            else:
                corrupted = True
                break
        if corrupted:
            continue

        for o in opening[::-1]:
            line_tot = line_tot * 5 + value[flipped[o]]

        totals.append(line_tot)

    return int(np.median(totals))


test_inpt = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

test_inpt = test_inpt.split()
assert fix_incomplete(test_inpt) == 288957

inpt = list(read_input(10))
assert fix_incomplete(inpt) == 4245130838
