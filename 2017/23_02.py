from collections import defaultdict


def cast(val, regs):
    """if int return int else return char"""
    try:
        return int(val)
    except ValueError as ve:
        return regs[val]


def run_cmd(line, regs, idx):
    """run a command"""
    try:
        cmd, x, y = line.split()
    except ValueError as ve:
        cmd, x = line.split()

    if idx == 16:
        regs['e'] = regs['b']
        return regs, idx
    # elif idx == 20:
    #     regs['d'] = regs['b']
    #     return regs, idx

    if cmd == 'set':          # set reg X to val Y
        regs[x] = cast(y, regs)
    elif cmd == 'mul':          # set reg X to X * Y
        regs[x] = regs[x] * cast(y, regs)
    elif cmd == 'sub':          # decrease reg X by val Y
        regs[x] -= cast(y, regs)
    elif cmd == 'jnz':          # jumps by Y if X > 0
        if cast(x, regs) != 0:
            idx += cast(y, regs) - 1

    return regs, idx


def duet(lines):
    """run all the commands"""
    regs = defaultdict(int)
    regs['a'] = 1
    idx = 0
    while idx < len(lines):
        if idx in [15, 25]:
            print(idx)
            print(regs)
        regs, idx = run_cmd(lines[idx], regs, idx)
        idx += 1

    return regs['h']


print(duet(open('input').read().splitlines()))
