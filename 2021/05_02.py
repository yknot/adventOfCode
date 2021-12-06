"""
Day 5 part 2
"""
from collections import defaultdict
from utils import read_input


def filter_lines(pts):
    new_pts = []
    for a, b in pts:
        if a[0] == b[0] or a[1] == b[1]:
            new_pts.append([a, b])
        elif abs(a[0] - b[0]) == abs(a[1] - b[1]):
            new_pts.append([a, b])

    return new_pts


def count_overlap(pts):
    pts = filter_lines(pts)

    visited = defaultdict(int)
    for a, b in pts:
        if a[0] == b[0]:
            if a[1] > b[1]:
                tmp_1 = b[1]
                while tmp_1 <= a[1]:
                    visited[(a[0], tmp_1)] += 1
                    tmp_1 += 1
            else:
                tmp_1 = a[1]
                while tmp_1 <= b[1]:
                    visited[(b[0], tmp_1)] += 1
                    tmp_1 += 1
        elif a[1] == b[1]:
            if a[0] > b[0]:
                tmp_0 = b[0]
                while tmp_0 <= a[0]:
                    visited[(tmp_0, a[1])] += 1
                    tmp_0 += 1
            else:
                tmp_0 = a[0]
                while tmp_0 <= b[0]:
                    visited[(tmp_0, b[1])] += 1
                    tmp_0 += 1
        else:
            tmp_0, tmp_1 = b[0], b[1]
            if a[0] > b[0]:
                while tmp_0 <= a[0]:
                    visited[(tmp_0, tmp_1)] += 1
                    tmp_0 += 1
                    if a[1] > b[1]:
                        tmp_1 += 1
                    elif a[1] < b[1]:
                        tmp_1 -= 1

            elif a[0] < b[0]:
                while tmp_0 >= a[0]:
                    visited[(tmp_0, tmp_1)] += 1
                    tmp_0 -= 1
                    if a[1] > b[1]:
                        tmp_1 += 1
                    elif a[1] < b[1]:
                        tmp_1 -= 1

    tot = 0
    for _, v in visited.items():
        if v > 1:
            tot += 1
    return tot


def parser(line):
    front, back = line.split(" -> ")
    a, b = front.split(",")
    c, d = back.split(",")
    return [(int(a), int(b)), (int(c), int(d))]


test_inpt = list(read_input(5, file_template="{:02}_test_input", line_parser=parser))
assert count_overlap(test_inpt) == 12

inpt = list(read_input(5, line_parser=parser))
assert count_overlap(inpt) == 21406
