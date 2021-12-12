"""
Day 9, part 2
"""
from utils import read_input


def recurse_basin(inpt, i, j, visited):
    # already visited
    if (i, j) in visited:
        return 0
    # if found edge of basin
    if inpt[i][j] == 9:
        return 0

    visited.add((i, j))
    tot = 1
    # go up
    if i > 0:
        tot += recurse_basin(inpt, i - 1, j, visited)
    # go down
    if i < (len(inpt) - 1):
        tot += recurse_basin(inpt, i + 1, j, visited)
    # go left
    if j > 0:
        tot += recurse_basin(inpt, i, j - 1, visited)
    # go right
    if j < (len(inpt[i]) - 1):
        tot += recurse_basin(inpt, i, j + 1, visited)

    return tot


def find_basins(inpt):
    basins = []
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

            basins.append(recurse_basin(inpt, i, j, set()))

    a, b, c = sorted(basins)[-3:]
    tot = a * b * c
    return tot


def parser(inpt):
    return [int(i) for i in list(inpt.strip())]


test_inpt = """2199943210
3987894921
9856789892
8767896789
9899965678"""
test_inpt = [parser(line) for line in test_inpt.split()]
assert find_basins(test_inpt) == 1134

inpt = list(read_input(9, line_parser=parser))
assert find_basins(inpt) == 987840
