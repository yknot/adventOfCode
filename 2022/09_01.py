"""
Day 9
"""
from utils import read_input

test_inpt = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


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
    h_pos, t_pos = [0, 0], [0, 0]
    visited = set([tuple(t_pos)])

    for (d, n) in inpt:
        for _ in range(n):
            if d == "R":
                h_pos[0] += 1
            elif d == "L":
                h_pos[0] -= 1
            elif d == "U":
                h_pos[1] += 1
            elif d == "D":
                h_pos[1] -= 1

            t_pos = check_within_one(h_pos, t_pos)

            visited.add(tuple(t_pos))

    return len(visited)


def parser(line):
    d, n = line.split()
    return (d, int(n))


assert count_path([parser(l) for l in test_inpt.split("\n")]) == 13

inpt = read_input(9, line_parser=parser)
assert count_path(inpt) == 6470
