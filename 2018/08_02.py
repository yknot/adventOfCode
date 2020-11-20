"""
Day 8 part 2
"""

from utils import read_input


def calc_value(data, i=0):
    res = 0

    children = data[i]
    i += 1
    metadata = data[i]
    i += 1

    children_values = []
    for _ in range(children):
        c_res, i = calc_value(data, i)
        children_values.append(c_res)

    for _ in range(metadata):
        if children > 0:
            if data[i] - 1 < children and data[i] != 0:
                res += children_values[data[i] - 1]
        else:
            res += data[i]

        i += 1

    return res, i


def parser(line):
    return [int(l) for l in line.split(" ")]


test = parser("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
assert calc_value(test)[0] == 66

inpt = read_input(8, line_parser=parser)
assert calc_value(inpt)[0] == 37067
