"""
Day 8
"""
import numpy as np

test_inpt = """30373
25512
65332
33549
35390"""


def count_visible(grid):
    total = 2 * grid.shape[0] + 2 * grid.shape[1] - 4

    i = 1
    while i < (grid.shape[0] - 1):
        j = 1
        while j < (grid.shape[1] - 1):
            h = grid[i, j]
            up = grid[:i, j]
            down = grid[i + 1 :, j]
            left = grid[i, :j]
            right = grid[i, j + 1 :]
            if (
                (h > up).all()
                or (h > down).all()
                or (h > left).all()
                or (h > right).all()
            ):
                total += 1

            j += 1

        i += 1

    return total


def parser(inpt):
    return np.array([[int(i) for i in list(line)] for line in inpt.split()])


assert count_visible(parser(test_inpt)) == 21

with open("08_input") as f:
    inpt = parser(f.read())

assert count_visible(inpt) == 1805
