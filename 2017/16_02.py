def run_cmd(c, group):
    """run a command"""
    if c[0] == 's':
        end_idx = -int(c[1:])
        group = group[end_idx:] + group[:end_idx]
    elif c[0] == 'x':
        a, b = c[1:].split('/')
        group[int(b)], group[int(a)] = group[int(a)], group[int(b)]
    elif c[0] == 'p':
        a, b = c[1:].split('/')
        a_idx, b_idx = group.index(a), group.index(b)
        group[b_idx], group[a_idx] = group[a_idx], group[b_idx]

    return group


def commands(cmds, group):
    """run all of the commands"""
    i = 1
    while True:
        for c in cmds:
            group = run_cmd(c, group)

        if ''.join(group) == 'abcdefghijklmnop':
            break
        i += 1

    steps = 1000000000 % i
    for _ in range(steps):
        for c in cmds:
            group = run_cmd(c, group)

    return ''.join(group)


group = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

print(commands(open('input').read().split(','), group))
