import numpy as np

start = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])


def transform(grid, rules):
    """transform the grid"""
    g_sum = grid.sum()
    g_hash = hash(bytes(grid))
    for r in rules:
        if r.i_sum != g_sum:
            continue
        if r.i_hash == g_hash:
            return r.o_pat
    raise


class Rule(object):
    def __init__(self, i, o):
        self.i_pat = i
        self.i_hash = hash(bytes(i))
        self.i_sum = i.sum()
        self.o_pat = o


def converter(tmp):
    """convert string to bool"""
    res = np.zeros((len(tmp), len(tmp)))
    for i, line in enumerate(tmp):
        for j, val in enumerate(line):
            if val == '#':
                res[i, j] = 1
    return res.astype(int)


def parse_rules(raw):
    """parse the raw rules"""
    rules_2 = []
    rules_3 = []

    for r in raw:
        raw = r.split(' => ')
        in_pattern = converter(raw[0].split('/'))
        two_flag = True if len(in_pattern) == 2 else False
        out_pattern = converter(raw[1].split('/'))

        # add all rotations of rule
        for i in range(4):
            if two_flag:
                rules_2.append(Rule(in_pattern, out_pattern))
            else:
                rules_3.append(Rule(in_pattern, out_pattern))
            in_pattern = np.rot90(in_pattern)

        # flip then try again
        in_pattern = np.flip(in_pattern, 1)
        for i in range(4):
            if two_flag:
                rules_2.append(Rule(in_pattern, out_pattern))
            else:
                rules_3.append(Rule(in_pattern, out_pattern))
            in_pattern = np.rot90(in_pattern)

    return rules_2, rules_3


def split(g):
    if len(g) % 2 == 0:
        num_blocks = len(g) // 2
        block_size = 2
    else:
        num_blocks = len(g) // 3
        block_size = 3
    res = []
    for i in range(num_blocks):
        for j in range(num_blocks):
            res.append(g[(i * block_size):(i * block_size) + block_size,
                         (j * block_size):(j * block_size) + block_size])

    return res


def combine(gs):
    side_len = int(np.sqrt(len(gs)))
    k = 0
    res = np.array([])
    for i in range(side_len):
        res_sub = np.hstack((gs[k:k + side_len]))
        k += side_len
        res = res_sub if i == 0 else np.vstack((res, res_sub))

    return res


def run_algo(rules_raw, num_iter):
    """run the algorithm"""
    rules_2, rules_3 = parse_rules(rules_raw)
    grid = start

    for i in range(num_iter):
        if num_iter != 2:
            print(i, int(grid.sum()), len(grid))

        grids = split(grid)
        two_flag = True if len(grids[0]) == 2 else False
        new_grids = []
        for g in grids:
            new_grids.append(transform(g, rules_2 if two_flag else rules_3))

        grid = combine(new_grids)

    return grid


rules_raw = open('testinput').read().splitlines()
grid = run_algo(rules_raw, 2)
assert grid.sum() == 12

rules_raw = open('input').read().splitlines()
grid = run_algo(rules_raw, 18)
print(int(grid.sum()))
# double check
assert grid.sum() == 2355110
