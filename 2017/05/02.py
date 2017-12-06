

def navigate_maze(jumps):
    """take in the maze and navigate returning number of steps"""
    pos = 0
    steps = 0
    while pos < len(jumps):
        inc = jumps[pos]
        if jumps[pos] >= 3:
            jumps[pos] -= 1
        else:
            jumps[pos] += 1
        pos += inc
        steps += 1

    return steps


def parse_input(raw):
    """parse the inut"""
    return [int(r) for r in open(raw).read().split('\n')]


parsed = parse_input('test_input')
assert navigate_maze(parsed) == 10

parsed = parse_input('input')
print(navigate_maze(parsed))
