import copy
import sys


def add_steps(visited, steps, spot, idx, op):
    next_spot = copy.deepcopy(spot)
    for i in range(steps):
        if op == '+':
            next_spot[idx] += 1
        else:
            next_spot[idx] -= 1
        this_step = tuple(next_spot)
        if tuple(this_step) in visited:
            print(this_step)
            print(sum(abs(s) for s in this_step))
            sys.exit()
        else:
            print(this_step)
            visited.add(this_step)
    return visited


directions = open('input').read().splitlines()
directions = directions[0].split(', ')
# directions = ['R8', 'R4', 'R4', 'R8']
spot = [0, 0]
idx = 0
compass = 'N'
visited = set()
for d in directions:
    steps = int(d[1:])
    if d[0] == 'R':
        if compass in ['N', 'W']:
            add_steps(visited, steps, spot, idx, '+')
            spot[idx] += steps
            compass = 'E' if compass == 'N' else 'N'
        else:
            add_steps(visited, steps, spot, idx, '-')
            spot[idx] -= steps
            compass = 'S' if compass == 'E' else 'W'
    else:
        if compass in ['N', 'W']:
            add_steps(visited, steps, spot, idx, '-')
            spot[idx] -= steps
            compass = 'W' if compass == 'N' else 'S'
        else:
            add_steps(visited, steps, spot, idx, '+')
            spot[idx] += steps
            compass = 'N' if compass == 'E' else 'E'
    idx = int(not idx)
    # print(spot)

print(sum(abs(s) for s in spot))
