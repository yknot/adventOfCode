example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

xmas = "XMAS"


def parse_data(data):
    return [list(row) for row in data.split("\n")]


def start_search(i, j, grid):
    count = 0
    for direction in ["NW", "N", "NE", "E", "SE", "S", "SW", "W"]:
        if search(i, j, grid, "X", direction):
            count += 1
    return count


def search(i, j, grid, letter, direction):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return False
    if grid[i][j] != letter:
        return False

    idx = xmas.index(letter)
    if idx == len(xmas) - 1:
        return True

    if direction == "NW":
        return search(i - 1, j - 1, grid, xmas[idx + 1], direction)
    if direction == "N":
        return search(i - 1, j, grid, xmas[idx + 1], direction)
    if direction == "NE":
        return search(i - 1, j + 1, grid, xmas[idx + 1], direction)
    if direction == "E":
        return search(i, j + 1, grid, xmas[idx + 1], direction)
    if direction == "SE":
        return search(i + 1, j + 1, grid, xmas[idx + 1], direction)
    if direction == "S":
        return search(i + 1, j, grid, xmas[idx + 1], direction)
    if direction == "SW":
        return search(i + 1, j - 1, grid, xmas[idx + 1], direction)
    if direction == "W":
        return search(i, j - 1, grid, xmas[idx + 1], direction)


def find_xmas(data):
    grid = parse_data(data)

    xmas_count = 0
    for i, line in enumerate(grid):
        for j, col in enumerate(line):
            if col == "X":
                if res := start_search(i, j, grid):
                    xmas_count += res

    return xmas_count


def X_search(i, j, grid):
    if i - 1 < 0 or j - 1 < 0 or i + 1 >= len(grid) or j + 1 >= len(grid[0]):
        return False

    if (grid[i - 1][j - 1] == "M" and grid[i + 1][j + 1] == "S") or (
        grid[i - 1][j - 1] == "S" and grid[i + 1][j + 1] == "M"
    ):
        if (grid[i - 1][j + 1] == "M" and grid[i + 1][j - 1] == "S") or (
            grid[i - 1][j + 1] == "S" and grid[i + 1][j - 1] == "M"
        ):
            return True


def find_X_mas(data):
    grid = parse_data(data)

    xmas_count = 0
    for i, line in enumerate(grid):
        for j, col in enumerate(line):
            if col == "A":
                if X_search(i, j, grid):
                    xmas_count += 1

    return xmas_count


res = find_xmas(example)
assert res == 18, res

with open("04_input") as f:
    res = find_xmas(f.read())
    assert res == 2358, res


res = find_X_mas(example)
assert res == 9, res

with open("04_input") as f:
    res = find_X_mas(f.read())
    assert res == 1737, res
