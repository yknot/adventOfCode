"""
Day 9
"""
from utils import read_input


def find_low_points(inpt):
    low_points = []
    for i, line in enumerate(inpt):
        for j, cell in enumerate(line):
            if i > 0 and cell >= inpt[i - 1][j]:
                continue
            if i < (len(inpt) - 1) and cell >= inpt[i + 1][j]:
                continue
            if j > 0 and cell >= inpt[i][j - 1]:
                continue
            if j < (len(line) - 1) and cell >= inpt[i][j + 1]:
                continue

            low_points.append(cell)

    tot = sum([i + 1 for i in low_points])
    return tot


def parser(inpt):
    return [int(i) for i in list(inpt.strip())]


test_inpt = """2199943210
3987894921
9856789892
8767896789
9899965678"""
test_inpt = [parser(line) for line in test_inpt.split()]
assert find_low_points(test_inpt) == 15

inpt = list(read_input(9, line_parser=parser))
assert find_low_points(inpt) == 600
