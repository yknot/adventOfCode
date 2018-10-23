import numpy as np

from hash import hash_data


def defrag(input_str):
    """construct the defrag grid"""
    grid = np.zeros((128, 128))
    for i in range(128):
        h = hash_data(input_str + '-' + str(i))
        j = 0
        for val in h:
            tmp = [int(i) for i in bin(int(val, 16))[2:].zfill(4)]
            for k in range(4):
                grid[i, j + k] = tmp[k]
            j += 4

    return grid


def zero_out(i, j, grid):
    grid[i, j] = 0
    if i + 1 < 128 and grid[i + 1, j] == 1:
        zero_out(i + 1, j, grid)
    if i - 1 >= 0 and grid[i - 1, j] == 1:
        zero_out(i - 1, j, grid)
    if j + 1 < 128 and grid[i, j + 1] == 1:
        zero_out(i, j + 1, grid)
    if j - 1 >= 0 and grid[i, j - 1] == 1:
        zero_out(i, j - 1, grid)


def count_groups(grid):
    groups = 0
    for i in range(128):
        for j in range(128):
            if not grid[i, j]:
                continue
            groups += 1
            zero_out(i, j, grid)

    return groups


# test_grid = defrag('flqrgnkx')
test_grid = np.load('test_grid.npy')
assert np.sum(test_grid) == 8108
assert count_groups(test_grid) == 1242
# final_grid = defrag('wenycdww')
final_grid = np.load('final_grid.npy')
assert np.sum(final_grid) == 8226
print(count_groups(final_grid))
