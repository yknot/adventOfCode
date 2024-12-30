example_1 = """AAAA
BBCD
BBCC
EEEC"""

example_2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

example_3 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def parse_data(data):
    return [list(line) for line in data.split("\n")]


def expand_region(grid, i, j, val):
    region = set([(i, j)])
    region.update(expand(grid, region, i + 1, j, val))
    region.update(expand(grid, region, i - 1, j, val))
    region.update(expand(grid, region, i, j + 1, val))
    region.update(expand(grid, region, i, j - 1, val))

    return region


def expand(grid, region, i, j, val):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return region

    if (i, j) in region:
        return region

    if grid[i][j] != val:
        return region

    region.add((i, j))

    region.update(expand(grid, region, i + 1, j, val))
    region.update(expand(grid, region, i - 1, j, val))
    region.update(expand(grid, region, i, j + 1, val))
    region.update(expand(grid, region, i, j - 1, val))

    return region


def calculate_perimeter(region):
    perimeter = 0
    for x, y in list(region):
        if (x + 1, y) not in region:
            perimeter += 1
        if (x - 1, y) not in region:
            perimeter += 1
        if (x, y + 1) not in region:
            perimeter += 1
        if (x, y - 1) not in region:
            perimeter += 1

    return perimeter


def calculate_area_perimeter(grid):
    seen = set()

    regions = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            # if already visited skip
            if (i, j) in seen:
                continue
            seen.add((i, j))

            # if not visited, start a new region
            region = expand_region(grid, i, j, cell)
            seen.update(region)

            perimeter = calculate_perimeter(region)
            regions.append((cell, len(region), perimeter))

    total = 0
    for _, area, perimeter in regions:
        total += area * perimeter

    return total


def calculate_price(data):
    grid = parse_data(data)
    total = calculate_area_perimeter(grid)
    return total


res = calculate_price(example_1)
assert res == 140, res

res = calculate_price(example_2)
assert res == 772, res

res = calculate_price(example_3)
assert res == 1930, res

with open("12_input") as f:
    res = calculate_price(f.read())
    assert res == 1494342, res
