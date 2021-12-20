"""
Day 10
"""
from utils import read_input

flipped = {"(": ")", "[": "]", "{": "}", "<": ">"}
value = {")": 3, "]": 57, "}": 1197, ">": 25137}


def find_corrupted(inpt):
    tot = 0
    for line in inpt:
        opening = []
        for l in line:
            if l in ["(", "[", "{", "<"]:
                opening.append(l)
            elif l == flipped[opening[-1]]:
                opening.pop(-1)
            else:
                tot += value[l]
                break
    return tot


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
assert find_corrupted(test_inpt) == 26397

inpt = list(read_input(10))
assert find_corrupted(inpt) == 296535
