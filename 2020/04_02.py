"""
Day 4 part 1
"""

from utils import read_input


def valid_num(val, lo, hi):
    try:
        tmp = int(val)
    except:
        return False

    if tmp >= lo and tmp <= hi:
        return True

    return False


hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]


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

        new_pairs = {x.split(":")[0]: x.split(":")[1] for x in l.split()}
        for k, v in new_pairs.items():
            if k == "byr":
                if not valid_num(v, 1920, 2002):
                    continue
            elif k == "iyr":
                if not valid_num(v, 2010, 2020):
                    continue
            elif k == "eyr":
                if not valid_num(v, 2020, 2030):
                    continue
            elif k == "hgt":
                if v.endswith("cm"):
                    if not valid_num(v[:-2], 150, 193):
                        continue
                elif v.endswith("in"):
                    if not valid_num(v[:-2], 59, 76):
                        continue
                else:
                    continue
            elif k == "hcl":
                if not v.startswith("#"):
                    continue
                if len(v[1:]) != 6:
                    continue
                if any(x not in hex for x in v[1:]):
                    continue
            elif k == "ecl":
                if v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    continue
            elif k == "pid":
                if len(v) != 9:
                    continue
                try:
                    int(v)
                except:
                    continue
            else:
                continue

            curr.append(k)

    if not keys.difference(set(curr)):
        valid += 1

    return valid


test_input = read_input(4, file_template="{:02}_test_02")

assert validate_passport(test_input) == 4

inpt = read_input(4)

assert validate_passport(inpt) == 123
