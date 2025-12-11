from dataclasses import dataclass
from functools import lru_cache

example = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass
class Manifold:
    splitters: frozenset[Point]
    start: Point
    max_y: int

    def __hash__(self):
        return hash((self.splitters, self.start, self.max_y))

    def count_splits(self) -> int:
        splits = 0
        current_beams = set([self.start])

        # start on line 1 since the first line only contains the start beam
        for i in range(1, self.max_y):
            new_beams = set()
            for beam in current_beams:
                if Point(beam.x, beam.y + 1) in self.splitters:
                    splits += 1
                    new_beams.add(Point(beam.x - 1, beam.y + 1))
                    new_beams.add(Point(beam.x + 1, beam.y + 1))
                else:
                    new_beams.add(Point(beam.x, beam.y + 1))
            current_beams = new_beams

        return splits

    @lru_cache
    def count_single_splits(self, loc: Point | None = None) -> int:
        if loc is None:
            loc = self.start

        # base case
        if loc.y == self.max_y:
            return 1

        total = 0
        if loc in self.splitters:
            total += self.count_single_splits(Point(loc.x - 1, loc.y))
            total += self.count_single_splits(Point(loc.x + 1, loc.y))
            return total

        return self.count_single_splits(Point(loc.x, loc.y + 1))


def parse(inpt: str) -> Manifold:
    splitters = set()
    start = None
    for y, line in enumerate(inpt.splitlines()):
        for x, val in enumerate(line):
            if val == "S":
                start = Point(x, y)
            elif val == "^":
                splitters.add(Point(x, y))

    return Manifold(frozenset(splitters), start, len(inpt.splitlines()))


def count_beam_splits(inpt: str, single: bool = False) -> int:
    manifold = parse(inpt)

    if single:
        return manifold.count_single_splits()

    return manifold.count_splits()


with open("07_input") as f:
    data = f.read()

assert count_beam_splits(example) == 21
assert count_beam_splits(data) == 1490

assert count_beam_splits(example, single=True) == 40
assert count_beam_splits(data, single=True) == 3806264447357
