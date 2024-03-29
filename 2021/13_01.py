"""
Day 13
"""
from utils import read_input


def fold_vertically(points, line):
    for i, (x, y) in enumerate(points):
        if y >= line:
            points[i] = (x, line - (y - line))

    return points


def fold_horizontally(points, line):
    for i, (x, y) in enumerate(points):
        if x >= line:
            points[i] = (line - (x - line), y)

    return points


def make_grid(inpt):
    points = inpt[: inpt.index(None)]
    folds = inpt[inpt.index(None) + 1 :]

    fold = folds[0]
    if fold[0] == "x":
        points = fold_horizontally(points, fold[1])
    else:
        points = fold_vertically(points, fold[1])

    return len(set(points))


def parser(line):
    if "," in line:
        a, b = line.strip().split(",")
        return int(a), int(b)
    if line.startswith("fold"):
        last = line.strip().split()[-1]
        a, b = last.split("=")
        return a, int(b)
    return None


test_inpt = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

test_inpt = [parser(line) for line in test_inpt.split("\n")]
assert make_grid(test_inpt) == 17


inpt = list(read_input(13, line_parser=parser))
assert make_grid(inpt) == 790
