"""Day 3 part 1"""
from itertools import combinations, product


class Claim:
    """elf claim"""

    def __init__(self, line):
        ident, _, offset, shape = line.split()
        self.id = int(ident.lstrip('#'))
        self.lower = tuple([int(i.strip(':')) for i in offset.split(',')])
        self.shape = tuple([int(i.strip(':')) for i in shape.split('x')])
        self.upper = (self.lower[0] + self.shape[0],
                      self.lower[1] + self.shape[1])


def corner_checker(a, b, idx):
    """check one corner"""
    xs = []
    if a.lower[idx] < b.lower[idx]:
        x = min(a.upper[idx] - b.lower[idx], b.shape[idx])
        if x > 0:
            xs = range(b.lower[idx], b.lower[idx] + x)
    else:
        x = min(b.upper[idx] - a.lower[idx], a.shape[idx])
        if x > 0:
            xs = range(a.lower[idx], a.lower[idx] + x)

    return x, xs


def overlap_checker(a, b):
    """check for overlaps"""
    x, xs = corner_checker(a, b, 0)

    if x < 1:
        return []

    y, ys = corner_checker(a, b, 1)

    if y > 0:
        return product(xs, ys)

    return []


def find_total_overlaps(inpt):
    """driver function"""
    # read in all claims
    claims = []
    for l in inpt:
        claims.append(Claim(l))

    # develop a set of overlapping points
    overlaps = []
    for c, d in combinations(claims, 2):
        overlaps += overlap_checker(c, d)

    return len(set(overlaps))


if __name__ == "__main__":

    test = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""

    assert find_total_overlaps(test.split('\n')) == 4

    assert find_total_overlaps(open('03_input').readlines()) == 119572
