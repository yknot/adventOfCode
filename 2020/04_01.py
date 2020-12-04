"""
Day 4 part 1
"""

from utils import read_input


def validate_passport(lines):
    valid = 0
    keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    curr = []
    for l in lines:
        # if newline reset
        if l == "":
            if not keys.difference(set(curr)):
                valid += 1
            curr = []
            continue

        curr.extend([x.split(":")[0] for x in l.split()])

    if not keys.difference(set(curr)):
        valid += 1

    return valid


test_input = read_input(4, file_template="{:02}_test")

assert validate_passport(test_input) == 2

inpt = read_input(4)

assert validate_passport(inpt) == 206
