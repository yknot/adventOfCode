"""
Day 2 part 2
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
    hor, depth, aim = 0, 0, 0
    for d, i in dirs:
        if d == "forward":
            hor += int(i)
            depth += aim * int(i)
        elif d == "up":
            aim -= int(i)
        elif d == "down":
            aim += int(i)

    return hor * depth


inpt = list(read_input(2))

assert find_position(test_inpt) == 900

assert find_position(inpt) == 1872757425
