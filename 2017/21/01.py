start = ['.#.', '..#', '###']


class Grid(object):
    def __init__(self, g, s):
        self.size = s
        self.grid = g

    def transform(self, rules):
        """transform the grid"""
        for r in rules:
            if r.i_pat.num_on() != self.num_on():
                continue
            if check_equal(self.grid, r.i_pat.grid):
                return r.o_pat
        raise

    def num_on(self):
        total = 0
        for g in self.grid:
            for l in g:
                if l == '#':
                    total += 1
        return total


class Rule(object):
    def __init__(self, i, o):
        """init"""
        self.i_pat = Grid(i, len(i))
        if len(o) == 3:
            self.o_pat = Grid(o, len(o))
        else:
            self.o_pat = []
            for j in range(4):
                tmp = ['', '']
                if j == 0:
                    tmp[0] = o[0][:2]
                    tmp[1] = o[1][:2]
                elif j == 1:
                    tmp[0] = o[0][2:]
                    tmp[1] = o[1][2:]
                elif j == 2:
                    tmp[0] = o[2][:2]
                    tmp[1] = o[3][:2]
                elif j == 3:
                    tmp[0] = o[2][2:]
                    tmp[1] = o[3][2:]

                self.o_pat.append(Grid(tmp, 2))


def check_equal(a, b):
    """grid equality"""
    # print(a)
    # print(b)
    # print()
    if len(a) != len(b):
        return False
    if a == b:
        return True
    return False


def rotate(tmp):
    """rotate a grid clockwise"""
    if len(tmp) == 2:
        new_tmp = ['', '']
        new_tmp[0] = tmp[1][0] + tmp[0][0]
        new_tmp[1] = tmp[1][1] + tmp[0][1]
    else:
        new_tmp = ['', '', '']
        new_tmp[0] = tmp[2][0] + tmp[1][0] + tmp[0][0]
        new_tmp[1] = tmp[2][1] + tmp[1][1] + tmp[0][1]
        new_tmp[2] = tmp[2][2] + tmp[1][2] + tmp[0][2]
    return new_tmp


def flip(tmp):
    """flip a grid"""
    new_tmp = []
    for t in tmp:
        new_tmp.append(t[::-1])
    return new_tmp


def parse_rules(raw):
    """parse the raw rules"""
    rules = []

    for r in raw:
        raw = r.split(' => ')
        in_pattern = raw[0].split('/')
        out_pattern = raw[1].split('/')

        # add all rotations of rule
        for i in range(4):
            rules.append(Rule(in_pattern, out_pattern))
            in_pattern = rotate(in_pattern)

        # flip then try again
        in_pattern = flip(in_pattern)
        for i in range(4):
            rules.append(Rule(in_pattern, out_pattern))
            in_pattern = rotate(in_pattern)

    return rules


def run_step(grids, rules):
    """run a step for the grids"""
    new_grids = []
    for g in grids:
        tmp = g.transform(rules)
        if type(tmp) == list:
            new_grids += tmp
        else:
            new_grids.append(tmp)

    return new_grids


def run_algo(rules_raw, num_iter):
    """run the algorithm"""
    rules = parse_rules(rules_raw)
    grid = Grid(start, 3)

    grids = [grid]
    for i in range(num_iter):
        grids = run_step(grids, rules)

    return grids


rules_raw = open('testinput').read().splitlines()
grids = run_algo(rules_raw, 2)
assert sum([g.num_on() for g in grids]) == 12

rules_raw = open('input').read().splitlines()
grids = run_algo(rules_raw, 5)
print(sum([g.num_on() for g in grids]))
