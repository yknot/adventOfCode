from copy import copy

def print_steps(m, steps):
    """print out the steps from the set"""
    x_max = max(x for x, y in steps)
    y_max = max(y for x, y in steps)

    grid = []
    for y_i in range(y_max + 1):
        line = ['.'] * (x_max + 1)
        for x, y in steps:
            if y == y_i:
                line[x] = 'O'
        for x in range(x_max):
            if not m.check_open(x, y_i):
                line[x] = '#'

        line = [str(y_i).zfill(2)] + line
        grid.append(''.join(line))

    grid = '\n'.join(grid)
    print(grid)
    print()


class MazeWalker(object):
    def __init__(self, num, coord):
        self.num = num
        self.x_final, self.y_final = coord
        self.x_pos = self.y_pos = 1
        self.min_steps = self.x_final * self.y_final
        self.min_steps_path = set()

    def check_open(self, x, y):
        """check if a specific coordinate is open"""
        val = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + self.num
        count = '{0:b}'.format(val).count('1')
        return True if count % 2 == 0 else False

    def solve(self):
        """taking in a favorite number and coordinates find minimum path"""
        self.solve_step(set(), self.x_pos, self.y_pos)
        print_steps(self, self.min_steps_path)
        return self.min_steps

    def solve_step(self, steps, x_pos, y_pos):
        """run a step"""
        # print_steps(self, steps)
        # base case found the final point
        if x_pos == self.x_final and y_pos == self.y_final:
            if len(steps) < self.min_steps:
                self.min_steps = len(steps)
                self.min_steps_path = copy(steps)
            return

        if len(steps) > self.min_steps:
            return

        # add our location
        steps.add((x_pos, y_pos))

        # try to go the four directions
        # x + 1
        if (x_pos + 1, y_pos) not in steps \
            and self.check_open(x_pos + 1, y_pos):
            self.solve_step(steps, x_pos + 1, y_pos)
        # y + 1
        if (x_pos, y_pos + 1) not in steps \
            and self.check_open(x_pos, y_pos + 1):
            self.solve_step(steps, x_pos, y_pos + 1)
        # x - 1
        if x_pos > 0 and (x_pos - 1, y_pos) not in steps \
            and self.check_open(x_pos - 1, y_pos):
            self.solve_step(steps, x_pos - 1, y_pos)
        # y - 1
        if y_pos > 0 and (x_pos, y_pos - 1) not in steps \
            and self.check_open(x_pos, y_pos - 1):
            self.solve_step(steps, x_pos, y_pos - 1)

        steps.remove((x_pos, y_pos))


# test input
m = MazeWalker(10, (7, 4))
assert m.solve() == 11

# final input
m = MazeWalker(1358, (31, 39))
print(m.solve())
