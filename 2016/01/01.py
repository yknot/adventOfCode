directions = open('input').read().splitlines()
directions = directions[0].split(', ')
spot = [0, 0]
idx = 0
compass = 'N'
for d in directions:
    steps = int(d[1:])
    if d[0] == 'R':
        if compass in ['N', 'W']:
            spot[idx] += steps
            compass = 'E' if compass == 'N' else 'N'
        else:
            spot[idx] -= steps
            compass = 'S' if compass == 'E' else 'W'
    else:
        if compass in ['N', 'W']:
            spot[idx] -= steps
            compass = 'W' if compass == 'N' else 'S'
        else:
            spot[idx] += steps
            compass = 'N' if compass == 'E' else 'E'
    idx = int(not idx)

print(sum(abs(s) for s in spot))
