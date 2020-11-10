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


def max_burst(pairs):
    min_x, max_x, min_y, max_y = get_borders(pairs)
    max_dist = dist_calc((min_x, min_y), (max_x, max_y))

    contains = {tuple(p): list() for p in pairs}
    exclude = []

    for x, y in product(range(min_x, max_x + 1), range(min_y, max_y + 1)):
        min_dist = max_dist
        min_pts = []
        for pt in contains.keys():
            res = dist_calc((x, y), pt)
            if res < min_dist:
                min_dist = res
                min_pts = [pt]
            elif res == min_dist:
                min_pts.append(pt)

        if len(min_pts) == 1:
            contains[min_pts[0]].append((x, y))

        if x in [min_x, max_x] or y in [min_y, max_y]:
            exclude.append((x, y))

    exclude = set(exclude)
    return max([len(v) for k, v in contains.items() if k not in exclude])


test_input = ([1, 1], [1, 6], [8, 3], [3, 4], [5, 5], [8, 9])

assert max_burst(test_input) == 17

# read input into coordinate pairs
full_input = read_input(
    6, line_parser=lambda x: [int(i) for i in x.strip().split(", ")]
)

assert max_burst(full_input) == 5626
