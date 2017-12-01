
instructions = open('input').read().split('\n')
reg = {'a': 0,
       'b': 0,
       'c': 0,
       'd': 0}

i = 0
while i < len(instructions):
    cmd = instructions[i].split()
    if cmd[0] == 'cpy':
        if cmd[1] in reg.keys():
            reg[cmd[2]] = reg[cmd[1]]
        else:
            reg[cmd[2]] = int(cmd[1])

    elif cmd[0] == 'inc':
        reg[cmd[1]] += 1

    elif cmd[0] == 'dec':
        reg[cmd[1]] -= 1

    elif cmd[0] == 'jnz':
        if cmd[1] in reg.keys():
            if reg[cmd[1]]:
                i += int(cmd[2])
                continue
        elif int(cmd[1]):
            i += int(cmd[2])
            continue

    i += 1
    # print(cmd, reg)

print(reg['a'])
