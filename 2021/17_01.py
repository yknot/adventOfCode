"""
Day 17
"""
from math import ceil
from itertools import product
from utils import read_input


def parse_inpt(inpt):
    splits = [t.strip("xy=,") for t in inpt.split() if ".." in t]
    x, y = [x.split("..") for x in splits]
    return (int(x[0]), int(x[1])), (int(y[0]), int(y[1]))


def find_min_x(edge):
    min_x = 0
    sum_x = 0
    while sum_x <= edge:
        min_x += 1
        sum_x += min_x

    return min_x


def test_velocity(x_vel, y_vel, x_range, y_range):
    max_y_pos = 0
    x_pos, y_pos = 0, 0

    while True:
        if y_pos > max_y_pos:
            max_y_pos = y_pos
        # check if in grid
        if x_range[0] <= x_pos <= x_range[1] and y_range[0] <= y_pos <= y_range[1]:
            return max_y_pos
        # check if past grid
        if y_pos < y_range[1] or x_pos > x_range[1]:
            return -1

        # step
        x_pos += x_vel
        y_pos += y_vel

        # decrease
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1

        y_vel -= 1


def get_velocity(inpt):
    x_range, y_range = parse_inpt(inpt)

    min_x = find_min_x(x_range[0])
    max_x = ceil(x_range[1] / 2) + 1
    x_vel_range = range(min_x, max_x + 1)

    min_y = 1
    max_y = abs(min(y_range)) + 1
    y_vel_range = range(min_y, max_y + 1)

    max_height = 0
    for x_vel, y_vel in product(x_vel_range, y_vel_range):
        height = test_velocity(x_vel, y_vel, x_range, y_range)
        if height > max_height:
            max_height = height

    return max_height


test_inpt = "target area: x=20..30, y=-10..-5"


assert get_velocity(test_inpt) == 45


inpt = read_input(17)
try:
    res = get_velocity(inpt)
    assert res == 11781
except:
    print(res)
    raise
