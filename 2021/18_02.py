"""
Day 18, part 2
"""
from math import floor, ceil
from itertools import product
from utils import read_input

DEBUG = False


def get_magnitude(line):
    result = 0
    mult = {0: 3, 1: 2}
    for i, l in enumerate(line):
        elem_type = type(l)
        if elem_type == list:
            result += mult[i] * get_magnitude(l)
        else:
            result += mult[i] * l

    return result


def addition(line_a, line_b):
    return f"[{line_a},{line_b}]"


def get_height(str_line):
    count = 0
    for i, s in enumerate(str_line):
        if s == "[":
            count += 1
        if s == "]":
            count -= 1
        if count >= 5:
            return i
    return None


def explode(str_line, start_idx=None):
    if not start_idx:
        start_idx = get_height(str_line)
    # get values
    end_idx = str_line.index("]", start_idx)
    left, right = str_line[start_idx : end_idx + 1].strip("[]").split(",")
    left, right = int(left), int(right)

    # get new left
    idx = start_idx
    while idx > 0 and not str_line[idx].isnumeric():
        idx -= 1
    if idx != 0:
        length = 1
        while str_line[idx - length].isnumeric():
            length += 1
        new_left = int(str_line[idx - length + 1 : idx + 1]) + int(left)
        beg = (
            str_line[: idx - length + 1] + str(new_left) + str_line[idx + 1 : start_idx]
        )
    else:
        beg = str_line[:start_idx]

    # get new right
    idx = end_idx
    new_right = None
    while idx < len(str_line) and not str_line[idx].isnumeric():
        idx += 1
    if idx != len(str_line):
        length = 1
        while str_line[idx + length].isnumeric():
            length += 1

        new_right = int(str_line[idx : idx + length]) + int(right)
        end = str_line[end_idx + 1 : idx] + str(new_right) + str_line[idx + length :]
    else:
        end = str_line[end_idx + 1 :]

    # put parts together
    return beg + str(0) + end


def find_split(str_line):
    idx = 1
    while idx < len(str_line):
        if str_line[idx - 1].isnumeric() and str_line[idx].isnumeric():
            return idx - 1
        idx += 1

    return None


def split(str_line, idx=None):
    if not idx:
        idx = find_split(str_line)

    length = 2
    while str_line[idx + length].isnumeric():
        length += 1

    # get beginning and ending
    beg = str_line[:idx]
    end = str_line[idx + length :]

    # get middle
    val = int(str_line[idx : idx + length])
    left = floor(val / 2)
    right = ceil(val / 2)
    mid = f"[{left},{right}]"

    return beg + mid + end


def solve_homework(inpt):
    max_mag = 0
    for i, j in product(inpt, inpt):
        if i == j:
            continue
        if DEBUG:
            print(i)
            print(j)

        result = addition(i, j)

        # check for explodes and splits
        while True:
            run = False
            if idx := get_height(str(result)):
                run = True
                result = explode(str(result), idx)
                # continue to the top and do explodes again
                continue
            if idx := find_split(str(result)):
                run = True
                result = split(str(result), idx)

            if not run:
                break

        mag = get_magnitude(eval(result))
        if DEBUG:
            print(result)
            print(mag)
            print()

        if mag > max_mag:
            max_mag = mag

    if DEBUG:
        print(f"final result is {max_mag}")
    return max_mag


test_inpt = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""


test_inpt = test_inpt.split("\n")
assert solve_homework(test_inpt) == 3993


inpt = read_input(18)
try:
    res = solve_homework(inpt)
    assert res == 4673
except:
    print(res)
    raise
