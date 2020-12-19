"""
Day 10 part 1

"""


from utils import read_input


def find_joltage(vals):
    vals = sorted(vals)

    ones = 0
    threes = 0

    prev = 0
    for v in vals:
        if v - prev == 1:
            ones += 1
        elif v - prev == 3:
            threes += 1

        prev = v

    return ones * (threes + 1)


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

assert find_joltage(test_inpt) == 7 * 5

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

assert find_joltage(test_inpt) == 22 * 10


inpt = read_input(10, line_parser=int)

assert find_joltage(inpt) == 1980
