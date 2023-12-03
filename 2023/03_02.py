"""
Day 3, part 2
"""
from utils import read_input
from collections import defaultdict

test_inpt = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def check_parts(lines):
    gears = defaultdict(list)

    for i, row in enumerate(lines):
        num = ""
        for j, col in enumerate(row):
            if not col.isdigit() or j + 1 == len(row):
                if num:
                    # special case for end of line
                    if j + 1 == len(row) and col.isdigit():
                        j += 1
                        num += col

                    # check right
                    if col == "*":
                        gears[(i, j)].append(int(num))
                    # check left
                    if j - len(num) - 1 >= 0 and row[j - len(num) - 1] == "*":
                        gears[(i, j - len(num) - 1)].append(int(num))
                    # check above and below
                    assert len(num) + 2 == len(list(range(j - len(num) - 1, j + 1)))
                    for idx in range(j - len(num) - 1, j + 1):
                        # check above
                        if i > 0 and idx >= 0 and idx < len(row):
                            if lines[i - 1][idx] == "*":
                                gears[(i - 1, idx)].append(int(num))
                        if i + 1 < len(lines) and idx >= 0 and idx < len(row):
                            if lines[i + 1][idx] == "*":
                                gears[(i + 1, idx)].append(int(num))

                num = ""

            else:
                num += col

    total = 0
    for _, v in gears.items():
        if len(v) == 2:
            total += v[0] * v[1]
    return total


inpt = list(read_input(3))

assert check_parts(test_inpt) == 467835

assert check_parts(inpt) == 69527306
