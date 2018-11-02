"""day 21 part 1"""


def swap(cmd, s):
    """execute both swap commands"""
    if cmd[1] == 'position':
        x = int(cmd[2])
        y = int(cmd[5])
        tmp = s[x]
        s[x] = s[y]
        s[y] = tmp
    else:
        x = cmd[2]
        y = cmd[5]
        s = ''.join(s)
        s = s.replace(x, ',')
        s = s.replace(y, x)
        s = s.replace(',', y)
        s = list(s)
    return s


def rotate(cmd, s):
    """execute both rotate commands"""
    if cmd[1] == 'based':
        x = s.index(cmd[6])
        if x >= 4:
            x += 1
        x += 1
        x %= len(s)
        s = s[-x:] + s[:-x]
    else:
        x = int(cmd[2]) % len(s)
        if cmd[1] == 'right':
            s = s[-x:] + s[:-x]
        else:
            s = s[x:] + s[:x]
    return s


def reverse(cmd, s):
    """reverse string in range"""
    x = int(cmd[2])
    y = int(cmd[4]) + 1
    return s[:x] + s[x:y][::-1] + s[y:]


def move(cmd, s):
    """run move command"""
    x = int(cmd[2])
    y = int(cmd[5])
    tmp = s.pop(x)
    s.insert(y, tmp)
    return s


def run_steps(steps, start):
    """run all the steps"""
    start = list(start)
    for step in steps:
        tok = step.split()
        if tok[0] == 'swap':
            start = swap(tok, start)
        elif tok[0] == 'rotate':
            start = rotate(tok, start)
        elif tok[0] == 'reverse':
            start = reverse(tok, start)
        elif tok[0] == 'move':
            start = move(tok, start)
        else:
            print('Error')

    return ''.join(start)


test = [
    'swap position 4 with position 0', 'swap letter d with letter b',
    'reverse positions 0 through 4', 'rotate left 1 step',
    'move position 1 to position 4', 'move position 3 to position 0',
    'rotate based on position of letter b',
    'rotate based on position of letter d'
]

assert run_steps(test, 'abcde') == 'decab'

print(run_steps(open('21_input').read().split('\n'), 'abcdefgh'))