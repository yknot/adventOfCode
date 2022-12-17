"""
Day 14
"""

from utils import read_input


def print_grid(grid, sand=None):
    x_coords = [x for x, _ in grid]
    min_x, max_x = min(x_coords), max(x_coords)
    max_y = max([y for _, y in grid])

    print(min_x, max_x, sep="\t")
    for i in range(max_y + 1):
        for j in range(min_x, max_x + 1):
            if (j, i) in grid:
                print("#", end="")
            elif sand and (j, i) in sand:
                print("O", end="")
            else:
                print(".", end="")
        print()


def create_grid(lines):
    grid = set()
    for line in lines:
        grid.add(line[0])
        for i, point in enumerate(line[1:]):
            if line[i][0] != point[0]:
                step = 1 if point[0] > line[i][0] else -1
                for x in range(line[i][0], point[0], step):
                    grid.add((x, point[1]))
            elif line[i][1] != point[1]:
                step = 1 if point[1] > line[i][1] else -1
                for y in range(line[i][1], point[1], step):
                    grid.add((point[0], y))
            grid.add(point)

    return grid


def run_sand(grid):
    sand = set()
    max_y = max([y for _, y in grid])
    while True:
        x, y = 500, 0

        while True:
            # sand falling too far
            if y > max_y:
                break
            # try to move down
            elif (x, y + 1) not in grid and (x, y + 1) not in sand:
                y += 1
            # try to move diagonal left
            elif (x - 1, y + 1) not in grid and (x - 1, y + 1) not in sand:
                x -= 1
                y += 1
            # try to move diagonal right
            elif (x + 1, y + 1) not in grid and (x + 1, y + 1) not in sand:
                x += 1
                y += 1
            # can't move
            else:
                sand.add((x, y))
                break

        if y > max_y:
            break

    # print_grid(grid, sand)
    return len(sand)


def count_sand(inpt):
    grid = create_grid(inpt)
    # print_grid(grid)
    count = run_sand(grid)

    return count


test_inpt = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def parser(line):
    instructions = line.strip().split(" -> ")
    return [(int(i.split(",")[0]), int(i.split(",")[1])) for i in instructions]


assert count_sand([parser(line) for line in test_inpt.split("\n")]) == 24

assert count_sand(read_input(14, line_parser=parser)) == 638
