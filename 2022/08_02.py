"""
Day 8
"""
import numpy as np

test_inpt = """30373
25512
65332
33549
35390"""


def compute_scenic(grid):
    scenic = np.zeros(grid.shape)

    i = 1
    while i < (grid.shape[0] - 1):
        j = 1
        while j < (grid.shape[1] - 1):
            h = grid[i, j]
            up = grid[:i, j][::-1]
            down = grid[i + 1 :, j]
            left = grid[i, :j][::-1]
            right = grid[i, j + 1 :]

            total = 1
            for lst in [up, down, left, right]:
                for c, x in enumerate(lst):
                    if x >= h:
                        total *= c + 1
                        break
                else:
                    total *= len(lst)

            scenic[i, j] = total

            j += 1

        i += 1

    return int(scenic.max())


def parser(inpt):
    return np.array([[int(i) for i in list(line)] for line in inpt.split()])


assert compute_scenic(parser(test_inpt)) == 8

with open("08_input") as f:
    inpt = parser(f.read())

assert compute_scenic(inpt) == 444528
