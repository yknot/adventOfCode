"""
Day 3
"""
from utils import read_input


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
    total = 0

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
                    if col != "." and not col.isdigit():
                        total += int(num)
                    # check left
                    elif (
                        j - len(num) - 1 >= 0
                        and row[j - len(num) - 1] != "."
                        and not row[j - len(num) - 1].isdigit()
                    ):
                        total += int(num)
                    # check above and below
                    assert len(num) + 2 == len(list(range(j - len(num) - 1, j + 1)))
                    for idx in range(j - len(num) - 1, j + 1):
                        # check above
                        if i > 0 and idx >= 0 and idx < len(row):
                            if (
                                lines[i - 1][idx] != "."
                                and not lines[i - 1][idx].isdigit()
                            ):
                                total += int(num)
                                break
                        if i + 1 < len(lines) and idx >= 0 and idx < len(row):
                            if (
                                lines[i + 1][idx] != "."
                                and not lines[i + 1][idx].isdigit()
                            ):
                                total += int(num)
                                break

                num = ""

            else:
                num += col

    return total


inpt = list(read_input(3))

assert check_parts(test_inpt) == 4361

assert check_parts(inpt) == 521515
