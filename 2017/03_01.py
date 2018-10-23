
def make_grid(input_val):
    """make the spiral memory grid"""

    coord = [0, 0]
    grid = {1: tuple(coord)}
    val = 1
    level = 1
    while val <= input_val:
        # move to new grid
        coord[0] += 1
        val += 1
        grid[val] = tuple(coord)

        # southeast to northeast
        while coord[1] < level:
            coord[1] += 1
            val += 1
            grid[val] = tuple(coord)

        # northeast to northwest
        while coord[0] > -level:
            coord[0] -= 1
            val += 1
            grid[val] = tuple(coord)

        # northwest to southwest
        while coord[1] > -level:
            coord[1] -= 1
            val += 1
            grid[val] = tuple(coord)

        # southwest to southeast
        while coord[0] < level:
            coord[0] += 1
            val += 1
            grid[val] = tuple(coord)

        level += 1

    return grid


def get_dist(grid, val):
    """calculate the manhattan distance"""
    coord = grid[val]
    return abs(coord[0]) + abs(coord[1])


input_val = 312051

grid = make_grid(input_val)

assert get_dist(grid, 1) == 0
assert get_dist(grid, 12) == 3
assert get_dist(grid, 23) == 2
assert get_dist(grid, 1024) == 31
print(get_dist(grid, input_val))
