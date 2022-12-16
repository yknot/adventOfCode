"""
Day 13
"""
from functools import cmp_to_key


def check_pair(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            ret = check_pair(l, r)
            if ret in [-1, 1]:
                return ret

        if len(left) < len(right):
            return -1
        elif len(left) > len(right):
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, int):
        return check_pair(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return check_pair([left], right)


def check_order(inpt):
    inpt.append([[2]])
    inpt.append([[6]])
    inpt_sort = sorted(inpt, key=cmp_to_key(check_pair))

    total = 1
    for i, line in enumerate(inpt_sort):
        if line == [[2]]:
            total *= i + 1
        if line == [[6]]:
            total *= i + 1

    return total


test_inpt = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def parser(line):
    if line:
        return eval(line)
    return None


test_parsed = [parser(line) for line in test_inpt.split()]
assert check_order(test_parsed) == 140

parsed = []
with open("13_input") as f:
    for line in f:
        if line.strip():
            parsed.append(parser(line.strip("\n")))
assert check_order(parsed) == 22425
