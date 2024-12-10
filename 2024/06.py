example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def parse_data(data):
    marked = set()
    split_data = data.split()
    height = len(split_data)
    width = len(split_data[0])
    start = None

    for i, row in enumerate(split_data):
        for j, cell in enumerate(row):
            if cell == "#":
                marked.add((i, j))
            elif cell == "^":
                start = (i, j)

    return marked, height, width, start


def print_grid(marked, height, width, loc, seen):
    for i in range(height):
        row = []
        for j in range(width):
            if (i, j) in marked:
                row.append("#")
            elif (i, j) in seen:
                row.append("X")
            elif (i, j) == loc:
                row.append("^")
            else:
                row.append(".")

        print("".join(row))
    print()


def next_dir(direction):
    if direction == "N":
        return "E"
    if direction == "E":
        return "S"
    if direction == "S":
        return "W"
    if direction == "W":
        return "N"


direction_moves = {
    "N": lambda i, j: (i - 1, j),
    "E": lambda i, j: (i, j + 1),
    "S": lambda i, j: (i + 1, j),
    "W": lambda i, j: (i, j - 1),
}


def find_path(marked, height, width, start):
    direction = "N"
    i, j = start
    seen = set()
    loop = set()
    while i >= 0 and j >= 0 and i < height and j < width:
        # check if we are in an infinite loop
        if (i, j) in seen:
            if (i, j) in loop:
                return None
            loop.add((i, j))
        else:
            seen.add((i, j))
            loop = set()
        # print_grid(marked, height, width, (i, j), seen)

        while direction_moves[direction](i, j) in marked:
            direction = next_dir(direction)

        i, j = direction_moves[direction](i, j)

    return seen


def measure_path(data):
    marked, height, width, start = parse_data(data)
    seen = find_path(marked, height, width, start)
    return len(seen)


def find_loops(data):
    marked, height, width, start = parse_data(data)
    seen = find_path(marked, height, width, start)

    total = 0
    for i, j in seen:
        marked.add((i, j))
        if find_path(marked, height, width, start) is None:
            total += 1

        marked.remove((i, j))

    return total


res = measure_path(example)
assert res == 41, res


with open("06_input") as f:
    res = measure_path(f.read())
    assert res == 4890, res


res = find_loops(example)
assert res == 6, res


with open("06_input") as f:
    res = find_loops(f.read())
    assert res == 1995, res
