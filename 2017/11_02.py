import operator

moves = {
    'ne': [1, .5],
    'n': [0, 1],
    'nw': [-1, .5],
    'sw': [-1, -.5],
    's': [0, -1],
    'se': [1, -.5]
}


def move(loc, direction):
    if loc[1] > 0:
        loc = list(map(operator.add, loc, moves['s' + direction]))
        return loc, 1
    if loc[1] < 0:
        loc = list(map(operator.add, loc, moves['n' + direction]))
        return loc, 1

    return [0, 0], abs(loc[0])


def find_min_moves(loc):
    """find the minimum number of moves"""
    min_moves = 0
    while loc != [0, 0]:
        if loc[0] > 0:
            loc, res = move(loc, 'w')
            min_moves += res
            continue

        if loc[0] < 0:
            loc, res = move(loc, 'e')
            min_moves += res
            continue

        loc, res = move(loc, '')
        min_moves += res

    return min_moves


def min_steps(path):
    """find the minimum path"""
    # find end point
    loc = [0, 0]
    max_dist = 0
    prev_loc = [0, 0]
    for p in path:
        loc = list(map(operator.add, loc, moves[p]))

        if (abs(loc[0]) + abs(loc[1])) > (abs(prev_loc[0]) + abs(prev_loc[1])):
            res = find_min_moves(loc)
            if res > max_dist:
                max_dist = res

        prev_loc = loc

    return max_dist


# final run
puz_in = open('input').read().split(',')
print(min_steps(puz_in))
