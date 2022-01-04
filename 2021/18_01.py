"""
Day 18
"""
from math import floor, ceil
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
    if DEBUG:
        print(f"result of {line} = {result}")
    return result


def addition(line_a, line_b):
    if DEBUG:
        print(f"addition:\n\t{line_a}\n\t{line_b}")
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
    if DEBUG:
        print(f"pre-explode: {str_line}")
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
    if DEBUG:
        print(f"explode: beg: {beg}\t mid: {str(0)}\t end: {end}")
    return beg + str(0) + end


def find_split(str_line):
    idx = 1
    while idx < len(str_line):
        if str_line[idx - 1].isnumeric() and str_line[idx].isnumeric():
            return idx - 1
        idx += 1

    return None


def split(str_line, idx=None):
    if DEBUG:
        print(f"pre-split: {str_line}")
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

    if DEBUG:
        print(f"split: beg: {beg}\t mid: {mid}\t end: {end}")

    return beg + mid + end


def solve_homework(inpt):
    result = inpt[0]
    for i in inpt[1:]:
        result = addition(result, i)

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

        if DEBUG:
            print(result)
            print()

    mag = get_magnitude(eval(result))
    if DEBUG:
        print(f"final result is {mag}")
    return mag


assert get_magnitude([9, 1]) == 29
assert get_magnitude([1, 9]) == 21
assert get_magnitude([[9, 1], [1, 9]]) == 129
assert get_magnitude([[1, 2], [[3, 4], 5]]) == 143
assert get_magnitude([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]) == 1384.0
assert get_magnitude([[[[1, 1], [2, 2]], [3, 3]], [4, 4]]) == 445.0
assert get_magnitude([[[[3, 0], [5, 3]], [4, 4]], [5, 5]]) == 791.0
assert get_magnitude([[[[5, 0], [7, 4]], [5, 5]], [6, 6]]) == 1137.0
assert (
    get_magnitude([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]])
    == 3488
)
assert (
    get_magnitude(
        [[[[6, 6], [7, 6]], [[7, 7], [7, 0]]], [[[7, 7], [7, 7]], [[7, 8], [9, 9]]]]
    )
    == 4140
)

assert addition("[1,2]", "[[3,4],5]") == "[[1,2],[[3,4],5]]"

assert explode("[[[[[9,8],1],2],3],4]") == "[[[[0,9],2],3],4]"
assert explode("[7,[6,[5,[4,[3,2]]]]]") == "[7,[6,[5,[7,0]]]]"
assert explode("[[6,[5,[4,[3,2]]]],1]") == "[[6,[5,[7,0]]],3]"
assert (
    explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
    == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
)
assert explode("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]") == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"

assert split("[[[[0,7],4],[15,[0,13]]],[1,1]]") == "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"
assert (
    split("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")
    == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"
)


test_inpt = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""


test_inpt = test_inpt.split("\n")
assert solve_homework(test_inpt) == 3488

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
assert solve_homework(test_inpt) == 4140


inpt = read_input(18)
try:
    res = solve_homework(inpt)
    assert res == 4124
except:
    print(res)
    raise
