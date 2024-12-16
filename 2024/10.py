example = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def parse_data(data):
    result = []
    for d in data.split():
        result.append([int(i) for i in list(d)])

    return result


def find_zeros(grid):
    locs = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 0:
                locs.append((i, j))

    return locs


def find_path(grid, loc, val):
    if loc[0] < 0 or loc[1] < 0 or loc[0] >= len(grid) or loc[1] >= len(grid[0]):
        return None
    if grid[loc[0]][loc[1]] != val:
        return None
    if grid[loc[0]][loc[1]] == 9:
        return [loc]

    peaks = []
    res = find_path(grid, (loc[0] + 1, loc[1]), val + 1)
    if res:
        peaks += res
    res = find_path(grid, (loc[0] - 1, loc[1]), val + 1)
    if res:
        peaks += res
    res = find_path(grid, (loc[0], loc[1] + 1), val + 1)
    if res:
        peaks += res
    res = find_path(grid, (loc[0], loc[1] - 1), val + 1)
    if res:
        peaks += res

    return peaks


def find_ratings(grid, loc, val):
    if loc[0] < 0 or loc[1] < 0 or loc[0] >= len(grid) or loc[1] >= len(grid[0]):
        return 0
    if grid[loc[0]][loc[1]] != val:
        return 0
    if grid[loc[0]][loc[1]] == 9:
        return 1

    return (
        find_ratings(grid, (loc[0] + 1, loc[1]), val + 1)
        + find_ratings(grid, (loc[0] - 1, loc[1]), val + 1)
        + find_ratings(grid, (loc[0], loc[1] + 1), val + 1)
        + find_ratings(grid, (loc[0], loc[1] - 1), val + 1)
    )


def count_trails(data, find_rating=False):
    grid = parse_data(data)

    zeros_loc = find_zeros(grid)

    total = 0
    for loc in zeros_loc:
        if find_rating:
            total += find_ratings(grid, loc, 0)
        else:
            res = set(find_path(grid, loc, 0))
            total += len(res)

    return total


res = count_trails(example)
assert res == 36, res

with open("10_input") as f:
    res = count_trails(f.read())
    assert res == 566, res

res = count_trails(example, find_rating=True)
assert res == 81, res

with open("10_input") as f:
    res = count_trails(f.read(), find_rating=True)
    assert res == 566, res
