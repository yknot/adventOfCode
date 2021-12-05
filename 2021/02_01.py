"""
Day 2
"""
from utils import read_input


test_inpt = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def find_position(dirs):
    dirs = [i.split() for i in dirs]
    x_pos, y_pos = 0, 0
    for d, i in dirs:
        if d == "forward":
            x_pos += int(i)
        elif d == "up":
            y_pos -= int(i)
        elif d == "down":
            y_pos += int(i)

    return x_pos * y_pos


inpt = list(read_input(2))

assert find_position(test_inpt) == 150

assert find_position(inpt) == 1636725
