"""
Day 9
"""
from utils import read_input

test_inpt = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


def check_within_one(h_pos, t_pos):
    # move diagonal
    if abs(h_pos[0] - t_pos[0]) > 0 and abs(h_pos[1] - t_pos[1]) > 0:
        if (h_pos[0] - t_pos[0]) > 1:
            t_pos[0] += 1
            if (h_pos[1] - t_pos[1]) > 0:
                t_pos[1] += 1
            elif (t_pos[1] - h_pos[1]) > 0:
                t_pos[1] -= 1
        elif (t_pos[0] - h_pos[0]) > 1:
            t_pos[0] -= 1
            if (h_pos[1] - t_pos[1]) > 0:
                t_pos[1] += 1
            elif (t_pos[1] - h_pos[1]) > 0:
                t_pos[1] -= 1
        elif (h_pos[1] - t_pos[1]) > 1:
            t_pos[1] += 1
            if (h_pos[0] - t_pos[0]) > 0:
                t_pos[0] += 1
            elif (t_pos[0] - h_pos[0]) > 0:
                t_pos[0] -= 1
        elif (t_pos[1] - h_pos[1]) > 1:
            t_pos[1] -= 1
            if (h_pos[0] - t_pos[0]) > 0:
                t_pos[0] += 1
            elif (t_pos[0] - h_pos[0]) > 0:
                t_pos[0] -= 1
    # elif one behind in x
    elif abs(h_pos[0] - t_pos[0]) > 1:
        if (h_pos[0] - t_pos[0]) > 1:
            t_pos[0] += 1
        elif (t_pos[0] - h_pos[0]) > 1:
            t_pos[0] -= 1
    # elif one behind in y
    elif abs(h_pos[1] - t_pos[1]) > 1:
        if (h_pos[1] - t_pos[1]) > 1:
            t_pos[1] += 1
        elif (t_pos[1] - h_pos[1]) > 1:
            t_pos[1] -= 1
    return t_pos


def count_path(inpt):
    pts = [[0, 0] for _ in range(10)]
    visited = set([tuple(pts[-1])])

    for (d, n) in inpt:
        for _ in range(n):
            if d == "R":
                pts[0][0] += 1
            elif d == "L":
                pts[0][0] -= 1
            elif d == "U":
                pts[0][1] += 1
            elif d == "D":
                pts[0][1] -= 1

            for i, _ in enumerate(pts[:-1]):
                pts[i + 1] = check_within_one(pts[i], pts[i + 1])

            visited.add(tuple(pts[-1]))

    return len(visited)


def parser(line):
    d, n = line.split()
    return (d, int(n))


assert count_path([parser(l) for l in test_inpt.split("\n")]) == 36

inpt = read_input(9, line_parser=parser)
assert count_path(inpt) == 2658
