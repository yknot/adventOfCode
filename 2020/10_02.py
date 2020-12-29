"""
Day 10 part 2

"""


from utils import read_input, comb


def dig(vals, idx):
    # base case
    if idx == len(vals) - 1:
        return 1

    total = 0
    next_up = vals[idx : idx + 4]
    if vals[idx] + 1 in next_up:
        total += dig(vals, vals.index(vals[idx] + 1))
    if vals[idx] + 2 in next_up:
        total += dig(vals, vals.index(vals[idx] + 2))
    if vals[idx] + 3 in next_up:
        total += dig(vals, vals.index(vals[idx] + 3))

    return total


def find_joltage(vals):
    vals.append(0)
    vals.append(max(vals) + 3)
    vals = sorted(vals)

    groups = []

    prev = 0
    idx = 0
    group = []
    while idx < len(vals):
        if prev + 3 == vals[idx]:
            if len(group) > 2:
                groups.append(group)
            group = [vals[idx]]
        else:
            group.append(vals[idx])

        prev = vals[idx]
        idx += 1

    combs = 1
    for g in groups:
        # take or leave one
        if len(g) == 3 and g[0] + 3 >= g[-1]:
            combs *= sum([comb(1, i) for i in range(1, -1, -1)])
        # sequential 4 elements
        elif len(g) == 4 and g[0] + 3 == g[-1]:
            combs *= sum([comb(2, i) for i in range(2, -1, -1)])
        # sequential 5 elements
        elif len(g) == 5 and g[0] + 4 == g[-1]:
            combs *= sum([comb(3, i) for i in range(3, 0, -1)])
        else:
            print("Corner case not found", g)

    return combs


test_inpt = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4,
]

assert find_joltage(test_inpt) == 8

test_inpt = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]

assert find_joltage(test_inpt) == 19208


inpt = list(read_input(10, line_parser=int))

assert find_joltage(inpt) == 4628074479616
