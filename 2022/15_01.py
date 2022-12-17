"""
Day 15
"""
from utils import read_input


def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def find_beacon(inpt, line):
    scanners = {k: distance(k, v) for k, v in inpt}
    possible_intersections = set([v for _, v in inpt if v[1] == line])
    possible_intersections.union(set(k for k in scanners.keys() if k[1] == line))

    points = set()
    for (x, y), d in scanners.items():
        temp_x = x
        dist = distance((x, y), (temp_x, line))
        if d < dist:
            continue

        points.add((temp_x, line))
        i = 1
        while d >= (dist + i):
            points.add((temp_x - i, line))
            points.add((temp_x + i, line))
            i += 1

    for p in possible_intersections:
        points.remove(p)
    # print(points)
    print(len(points))
    return len(points)


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


assert find_beacon([parser(line) for line in test_inpt.split("\n")], 10) == 26

assert find_beacon(read_input(15, line_parser=parser), 2000000) == 5688618
