"""
Day 4
"""
from utils import read_input


test_inpt = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def overlaps(vals):
    count = 0
    for x, y in vals:
        if x[0] >= y[0] and x[1] <= y[1]:
            count += 1
        elif y[0] >= x[0] and y[1] <= x[1]:
            count += 1

    return count


def parse(line):
    x, y = line.split(",")
    x_1, x_2 = x.split("-")
    y_1, y_2 = y.split("-")

    return (int(x_1), int(x_2)), (int(y_1), int(y_2))


inpt = list(read_input(4, line_parser=parse))

test = [parse(t) for t in test_inpt.split("\n")]

assert overlaps(test) == 2

assert overlaps(inpt) == 567
