from itertools import combinations


def read_in(filename):
    """read in the input, space delim numbers"""
    return [[int(i) for i in r.split()]
            for r in open(filename).read().split('\n')]


def checksum(data):
    """calculate the checksum based on sum of diffs by row"""
    total = 0
    for row in data:
        for x, y in combinations(sorted(row, reverse=True), 2):

            if x % y == 0:
                total += int(x / y)
                break

    return total


raw = read_in('testinput_2')

assert checksum(raw) == 9

print(checksum(read_in('input')))
