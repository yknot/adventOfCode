

def read_in(filename):
    """read in the input, space delim numbers"""
    return [[int(i) for i in r.split()]
            for r in open(filename).read().split('\n')]


def checksum(data):
    """calculate the checksum based on sum of diffs by row"""
    total = 0
    for row in data:
        total += max(row) - min(row)

    return total


raw = read_in('testinput')

assert checksum(raw) == 18

print(checksum(read_in('input')))
