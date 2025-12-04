from dataclasses import dataclass

example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


@dataclass
class Grid:
    roll_points: set[tuple[int, int]]

    def find_accessible_rolls(self) -> set[tuple[int, int]]:
        accessible = set()
        for x, y in self.roll_points:
            adjacent = 0
            for inc_x, inc_y in NEIGHBORS:
                if (x + inc_x, y + inc_y) in self.roll_points:
                    adjacent += 1
                    if adjacent >= 4:
                        break

            if adjacent < 4:
                accessible.add((x, y))

        return accessible


def parse(inpt: str) -> Grid:
    rolls = set()
    for x, line in enumerate(inpt.split()):
        for y, char in enumerate(line):
            if char == "@":
                rolls.add((x, y))

    return Grid(rolls)


def count_accessible_rolls(inpt: str) -> int:
    grid = parse(inpt)

    rolls = grid.find_accessible_rolls()

    return len(rolls)


def remove_accessible_rolls(inpt: str) -> int:
    grid = parse(inpt)

    total_remove = 0
    while True:
        rolls = grid.find_accessible_rolls()
        if len(rolls) == 0:
            break

        total_remove += len(rolls)
        grid.roll_points.difference_update(rolls)

    return total_remove


with open("04_input") as f:
    data = f.read()


assert count_accessible_rolls(example) == 13
assert count_accessible_rolls(data) == 1344

assert remove_accessible_rolls(example) == 43
assert remove_accessible_rolls(data) == 8112
