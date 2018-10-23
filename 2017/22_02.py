import numpy as np

directions = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}


class Grid(object):
    def __init__(self, g, steps):
        self.g = g
        self.steps = steps

    def go_right(self):
        if self.d == 'up':
            self.d = 'right'
        elif self.d == 'right':
            self.d = 'down'
        elif self.d == 'down':
            self.d = 'left'
        elif self.d == 'left':
            self.d = 'up'

    def go_left(self):
        if self.d == 'up':
            self.d = 'left'
        elif self.d == 'left':
            self.d = 'down'
        elif self.d == 'down':
            self.d = 'right'
        elif self.d == 'right':
            self.d = 'up'

    def reverse(self):
        if self.d == 'up':
            self.d = 'down'
        elif self.d == 'left':
            self.d = 'right'
        elif self.d == 'down':
            self.d = 'up'
        elif self.d == 'right':
            self.d = 'left'

    def expand(self):
        """expand the grid"""
        self.x += 1
        self.y += 1

        self.g = np.pad(self.g, 1, 'constant', constant_values=0)

    def run_step(self):
        """run one step"""
        if self.x < 0 or self.y < 0 or \
           self.x >= self.g.shape[0] or self.y >= self.g.shape[1]:
            self.expand()

        # if infected, flag and turn right
        if self.g[self.x, self.y] == '#':
            self.g[self.x, self.y] = 'F'
            self.go_right()
            self.x += directions[self.d][0]
            self.y += directions[self.d][1]
            return False

        # if weakend, infect
        elif self.g[self.x, self.y] == 'W':
            self.g[self.x, self.y] = '#'
            self.x += directions[self.d][0]
            self.y += directions[self.d][1]
            return True

        # if flagged, clean
        elif self.g[self.x, self.y] == 'F':
            self.g[self.x, self.y] = '.'
            self.reverse()
            self.x += directions[self.d][0]
            self.y += directions[self.d][1]
            return False

        # else clean, infect and turn left
        else:
            self.g[self.x, self.y] = 'W'
            self.go_left()
            self.x += directions[self.d][0]
            self.y += directions[self.d][1]
            return False

    def run_algo(self):
        """run the algorithm for steps"""
        self.x = self.y = self.g.shape[0] // 2
        self.d = 'up'
        count = 0
        for _ in range(self.steps):
            if self.run_step():
                count += 1

        return count


def read_grid(filename):
    """read in the grid and make numpy array"""
    with open(filename) as infile:
        raw_grid = infile.read().splitlines()

    res = np.empty((len(raw_grid), len(raw_grid[0])), dtype=str)
    for i, line in enumerate(raw_grid):
        for j, val in enumerate(line):
            res[i, j] = val
    return res


test_grid_raw = read_grid('testinput')
test_grid = Grid(test_grid_raw.copy(), 100)
assert test_grid.run_algo() == 26

test_grid = Grid(test_grid_raw.copy(), 10000000)
assert test_grid.run_algo() == 2511944

grid_raw = read_grid('input')
grid = Grid(grid_raw, 10000000)
print(grid.run_algo())
