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


def min_steps(path):
    """find the minimum path"""
    # find end point
    loc = [0, 0]
    for p in path:
        loc = list(map(operator.add, loc, moves[p]))

    # find minimum number of moves back
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


# tests
assert min_steps(['ne', 'ne', 'ne']) == 3
assert min_steps(['ne', 'ne', 'sw', 'sw']) == 0
assert min_steps(['ne', 'ne', 's', 's']) == 2
assert min_steps(['se', 'sw', 'se', 'sw', 'sw']) == 3

# final run
puz_in = open('input').read().split(',')
print(min_steps(puz_in))
