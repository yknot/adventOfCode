"""
Day 6 part 1
"""
from itertools import product
from utils import read_input


def get_borders(pairs):
    xs = [x for x, _ in pairs]
    min_x = min(xs)
    max_x = max(xs)
    ys = [y for _, y in pairs]
    min_y = min(ys)
    max_y = max(ys)
    return min_x, max_x, min_y, max_y


def dist_calc(pt_1, pt_2):
    """Manhattan distance calc"""
    x_1, y_1 = pt_1
    x_2, y_2 = pt_2

    return abs(x_1 - x_2) + abs(y_1 - y_2)


def max_region(pairs, max_dist):
    min_x, max_x, min_y, max_y = get_borders(pairs)

    contains = {tuple(p): list() for p in pairs}
    count = 0

    for x, y in product(range(min_x, max_x + 1), range(min_y, max_y + 1)):
        dist = 0
        for pt in contains.keys():
            dist += dist_calc((x, y), pt)
            if dist > max_dist:
                break

        if dist < max_dist:
            count += 1

    return count


test_input = ([1, 1], [1, 6], [8, 3], [3, 4], [5, 5], [8, 9])

assert max_region(test_input, 32) == 16

# read input into coordinate pairs
full_input = read_input(
    6, line_parser=lambda x: [int(i) for i in x.strip().split(", ")]
)

assert max_region(full_input, 10000) == 46554
