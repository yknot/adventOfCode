import sys


def do_op(register, op, a, b):
    if register == 'a':
        a = op(a)
    elif register == 'b':
        b = op(b)
    else:
        print("error bad register")
        sys.exit()
    return a, b


def check_reg(register, check, a, b):
    if register == 'a':
        return check(a)
    elif register == 'b':
        return check(b)
    else:
        print("error bad register")
        sys.exit()

data = [line.rstrip() for line in open('input')]
# data = ['inc a', 'jio a, +2', 'tpl a', 'inc a']

a = 0
b = 0

i = 0
while i < len(data):
    cmd = data[i].split(' ')

    if cmd[0] == 'hlf':
        a, b = do_op(cmd[1], lambda x: x//2, a, b)
    elif cmd[0] == 'tpl':
        a, b = do_op(cmd[1], lambda x: x*3, a, b)
    elif cmd[0] == 'inc':
        a, b = do_op(cmd[1], lambda x: x+1, a, b)
    elif cmd[0] == 'jmp':
        offset = int(cmd[1])
        i += offset
        continue
    elif cmd[0] == 'jie':
        if check_reg(cmd[1].strip(','), lambda x: x % 2 == 0, a, b):
            i += int(cmd[2])
            continue
    elif cmd[0] == 'jio':
        if check_reg(cmd[1].strip(','), lambda x: x == 1, a, b):
            i += int(cmd[2])
            continue
    else:
        print("error bad command")
        sys.exit()

    i += 1







print('register a: ' + str(a))
print('register b: ' + str(b))
