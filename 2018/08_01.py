"""
Day 8 part 1
"""

from utils import read_input


def calc_metadata(data, i=0):
    res = 0

    children = data[i]
    i += 1
    metadata = data[i]
    i += 1

    for _ in range(children):
        c_res, i = calc_metadata(data, i)
        res += c_res

    for _ in range(metadata):
        res += data[i]
        i += 1

    return res, i


def parser(line):
    return [int(l) for l in line.split(" ")]


test = parser("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
assert calc_metadata(test)[0] == 138

inpt = read_input(8, line_parser=parser)
assert calc_metadata(inpt)[0] == 40984
