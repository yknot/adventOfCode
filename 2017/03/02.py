from itertools import product


def calc_val(grid, coord):
    """sum surrounding squares"""
    x, y = coord
    dirs = [0, -1, 1]
    total = 0
    for x_inc, y_inc in product(dirs, dirs):
        tmp_coord = (x + x_inc, y + y_inc)
        if tmp_coord in grid:
            total += grid[tmp_coord]

    return total


def make_grid(input_val):
    """make the spiral memory grid"""

    coord = [0, 0]
    grid = {tuple(coord): 1}
    level = 1
    val = 1
    while val <= input_val:
        # move to new grid
        coord[0] += 1
        val = calc_val(grid, tuple(coord))
        grid[tuple(coord)] = val
        if val > input_val:
            return grid

        # southeast to northeast
        while coord[1] < level:
            coord[1] += 1
            val = calc_val(grid, tuple(coord))
            grid[tuple(coord)] = val
            if val > input_val:
                return grid

        # northeast to northwest
        while coord[0] > -level:
            coord[0] -= 1
            val = calc_val(grid, tuple(coord))
            grid[tuple(coord)] = val
            if val > input_val:
                return grid

        # northwest to southwest
        while coord[1] > -level:
            coord[1] -= 1
            val = calc_val(grid, tuple(coord))
            grid[tuple(coord)] = val
            if val > input_val:
                return grid

        # southwest to southeast
        while coord[0] < level:
            coord[0] += 1
            val = calc_val(grid, tuple(coord))
            grid[tuple(coord)] = val
            if val > input_val:
                return grid

        level += 1

    return grid


def get_dist(grid, val):
    """calculate the manhattan distance"""
    coord = grid[val]
    return abs(coord[0]) + abs(coord[1])


input_val = 312051

grid = make_grid(input_val)

grid = {v: k for k, v in grid.items()}

print(max(grid.keys()))
