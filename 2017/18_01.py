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

    if cmd == 'snd':            # play sound of freq X
        regs['last'] = regs[x]
    elif cmd == 'set':          # set reg X to val Y
        regs[x] = cast(y, regs)
    elif cmd == 'add':          # increase reg X by val Y
        regs[x] += cast(y, regs)
    elif cmd == 'mul':          # set reg X to X * Y
        regs[x] = regs[x] * cast(y, regs)
    elif cmd == 'mod':          # set reg X to X mod Y
        regs[x] = regs[x] % cast(y, regs)
    elif cmd == 'rcv':          # recover freq of last sound played if X != 0
        return regs['last'], idx
    elif cmd == 'jgz':          # jumps by Y if X > 0
        if cast(x, regs) > 0:
            idx += cast(y, regs) - 1
    return regs, idx


def duet(lines):
    """run all the commands"""
    regs = defaultdict(int)
    idx = 0
    while idx < len(lines):
        regs, idx = run_cmd(lines[idx], regs, idx)
        if type(regs) == int:
            return regs
        idx += 1


assert duet(open('testinput').read().splitlines()) == 4

print(duet(open('input').read().splitlines()))
