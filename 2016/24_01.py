"""day 24 part 1"""
import time
from collections import namedtuple
from itertools import combinations, permutations

Location = namedtuple('Location', ['x', 'y', 'n'])


def parse_puzzle(p):
    """parse the puzzle"""
    nums = {}
    blocked = set()

    for i, line in enumerate(p):
        for j, l in enumerate(line):
            if l == '#':
                blocked.add((i, j))
            elif l != '.':
                nums[int(l)] = (i, j)

    return nums, blocked


class Puzzle():
    """Puzzle class"""

    def __init__(self, inpt):
        self.nums, self.blocked = parse_puzzle(inpt)
        self.shape = (len(inpt[0]), len(inpt))

    def solve(self):
        """main solve method"""

        # find all min dists
        dists = {}
        for s, e in combinations(self.nums.keys(), 2):
            dist = self.find_dist(self.nums[s], self.nums[e])
            dists[(s, e)] = dist
            dists[(e, s)] = dist

        # find min covering path
        start = time.time()
        res = self.brute_force(dists)
        print(f'Brute Force: {time.time() - start}')
        print(res)

        start = time.time()
        res = self.min_covering(dists)
        print(f'Algo: {time.time() - start}')
        print(res)

        return res

    def find_dist(self, start, end):
        """find the minimum distance between two points"""
        queue = [Location(start[0], start[1], 0)]
        visited = {start}
        # breadth first search
        while queue:
            loc = queue.pop(0)

            # try all 4 directions
            for new_loc in [(loc.x + 1, loc.y), (loc.x - 1, loc.y),
                            (loc.x, loc.y + 1), (loc.x, loc.y - 1)]:

                # make sure we haven't been there or it's blocked
                if new_loc not in self.blocked and new_loc not in visited:
                    # if at the end then return
                    if new_loc == end:
                        return loc.n + 1
                    # add to list and visited
                    queue.append(Location(new_loc[0], new_loc[1], loc.n + 1))
                    visited.add(new_loc)

        raise ValueError

    def brute_force(self, dists):
        """brute force method"""
        vals = list(self.nums.keys())
        vals.remove(0)
        best = 100000
        order = None
        for p in permutations(vals):
            tot = dists[(0, p[0])]
            for i, v in enumerate(p[1:]):
                tot += dists[(p[i], v)]
            if tot < best:
                best = tot
                order = p

        print(order)
        return best

    def min_covering(self, dists):
        """run TSP w/o end algo"""
        vals = list(self.nums.keys())
        vals.remove(0)
        c = {}
        for v in vals:
            c[((v, ), v)] = dists[(0, v)]

        for s in range(2, len(vals) + 1):
            for p in permutations(vals, s):
                for v in p:
                    sub_p = list(p)
                    sub_p.remove(v)
                    sub_p = tuple(sub_p)
                    c[(p, v)] = min(
                        [c[(sub_p, m)] + dists[(m, v)] for m in sub_p])

        return min([v for k, v in c.items() if len(k[0]) == len(vals)])


if __name__ == '__main__':
    test = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########"""
    assert Puzzle(test.split('\n')).solve() == 14
    assert Puzzle(open('24_input').read().split('\n')).solve() == 470
