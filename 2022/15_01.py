"""
Day 15
"""
from utils import read_input


def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def find_beacon(inpt, line):
    scanners = {k: distance(k, v) for k, v in inpt}
    beacons = set([v for _, v in inpt])
    start = (sum([i[0][0] for i in inpt]) // len(inpt), line)
    total = 0
    # check left
    i = 0
    while True:
        if (start[0] - i, start[1]) in beacons:
            i += 1
            continue
        for s, d in scanners.items():
            # if as close or closer then can't exist

            if d >= distance(s, (start[0] - i, start[1])):
                total += 1
                break
        else:
            print(start[0] - i)
            break
        i += 1

    i = 1
    # chek right
    while True:
        if (start[0] + i, start[1]) in beacons:
            i += 1
            continue
        for s, d in scanners.items():
            # if as close or closer then can't exist
            if d >= distance(s, (start[0] + i, start[1])):
                total += 1
                break
        else:
            print(start[0] + i)
            break

        i += 1

    print(total)
    return total


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
