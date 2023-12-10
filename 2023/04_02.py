"""
Day 4
"""
from utils import read_input

test_inpt = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


def check_tickets(lines):
    multiplier = {i: 1 for i in range(len(lines))}

    for i, (win, mine) in enumerate(lines):
        mult = multiplier[i]
        matches = 0
        for m in mine:
            if m in win:
                matches += 1

        for j in range(matches):
            multiplier[i + j + 1] += mult

    return sum(multiplier.values())


def parser(line):
    mode = 0
    before = []
    after = []
    for l in line.split():
        if mode == 0 and l.endswith(":"):
            mode = 1
        elif mode == 1:
            if l == "|":
                mode = 2
            else:
                before.append(int(l))
        elif mode == 2:
            after.append(int(l))

    return [before, after]


inpt = list(read_input(4, line_parser=parser))

assert check_tickets([parser(x) for x in test_inpt]) == 30

assert check_tickets(inpt) == 5667240
