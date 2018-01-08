import numpy as np


def cast(s):
    triple = s.split('<')[1][:-1].split(',')
    triple = [int(t) for t in triple]
    return np.array(triple)


class Point(object):
    def __init__(self, split):
        """initalize"""
        self.loc = cast(split[0])
        self.vel = cast(split[1])
        self.acc = cast(split[2])

    def move(self):
        """move the point"""
        self.vel += self.acc
        self.loc += self.vel
        return self.loc


raw = open('input').read().splitlines()
points = {}

# build points
for i, r in enumerate(raw):
    split = r.split(', ')
    points[i] = Point(split)

step = 0
prev_len = 0
while True:
    if step % 100 == 0:
        print('{}\t{}'.format(step, len(points)))
        if prev_len == len(points):
            break
        prev_len = len(points)
    keys = np.zeros(len(points))
    vals = np.zeros((len(points), 3))
    i = 0
    # move everything
    for k, v in points.items():
        keys[i] = k
        vals[i] = v.move()
        i += 1

    # check for unique indexes
    out = np.unique(vals, axis=0, return_index=True, return_counts=True)
    # make sure there is only one of the unique value
    uniq_indexes = [o for i, o in enumerate(out[1]) if out[2][i] == 1]
    # find the inverse of the unique indexes
    remove = np.setdiff1d(range(len(points)), uniq_indexes)

    # remove the dups but make sure to map back to the keys
    for r in remove:
        del points[keys[r]]

    step += 1
