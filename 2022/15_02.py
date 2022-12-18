"""
Day 15
"""
from utils import read_input
from itertools import combinations


def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def find_beacon(inpt, mx):
    scanners = {k: distance(k, v) for k, v in inpt}
    beacons = set([v for _, v in inpt])

    # for each combination of diamonds
    for (x1, y1), s2 in combinations(scanners.keys(), 2):
        d1 = scanners[(x1, y1)] + 1
        d2 = scanners[s2] + 1

        iterations = (
            list(zip(range(-d1, 0), range(0, d1)))
            + list(zip(range(0, d1), range(d1, 0, -1)))
            + list(zip(range(d1, 0, -1), range(0, -d1, -1)))
            + list(zip(range(0, -d1, -1), range(-d1, 0, -1)))
        )
        # look around border of first diamond
        for x, y in iterations:
            i, j = x1 + x, y1 + y

            if i < 0 or i > mx or j < 0 or j > mx:
                continue
            # confirm point is one beyond border of second diamond
            if distance(s2, (i, j)) != d2:
                continue
            # if not the location of an existing beacon or scanner
            if (i, j) in beacons or (i, j) in scanners:
                continue
            # double check not within other scanners
            for s, d in scanners.items():
                if d >= distance(s, (i, j)):
                    break
            else:
                return i * 4000000 + j


test_inpt = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


def parser(line):
    vals = [int(l.strip(",:").split("=")[-1]) for l in line.split() if "=" in l]
    return (vals[0], vals[1]), (vals[2], vals[3])


test_scanners = [parser(line) for line in test_inpt.split("\n")]
assert find_beacon(test_scanners, 20) == 56000011

assert find_beacon(read_input(15, line_parser=parser), 4000000) == 12625383204261
