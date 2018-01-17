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

    mul_flag = False

    if cmd == 'set':          # set reg X to val Y
        regs[x] = cast(y, regs)
    elif cmd == 'mul':          # set reg X to X * Y
        regs[x] = regs[x] * cast(y, regs)
        mul_flag = True
    elif cmd == 'sub':          # decrease reg X by val Y
        regs[x] -= cast(y, regs)
    elif cmd == 'jnz':          # jumps by Y if X > 0
        if cast(x, regs) != 0:
            idx += cast(y, regs) - 1

    return regs, idx, mul_flag


def duet(lines):
    """run all the commands"""
    regs = defaultdict(int)
    idx = 0
    mul_count = 0
    while idx < len(lines):
        regs, idx, mul_flag = run_cmd(lines[idx], regs, idx)
        mul_count += int(mul_flag)
        idx += 1

    return mul_count


print(duet(open('input').read().splitlines()))
