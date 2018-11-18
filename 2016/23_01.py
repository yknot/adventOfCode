"""day 23 part 1"""


def run_instructions(instructions, a=0):
    reg = {'a': a, 'b': 0, 'c': 0, 'd': 0}

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
                if cmd[2] in reg.keys():
                    i += int(reg[cmd[2]])
                else:
                    i += int(cmd[2])
                continue
        elif cmd[0] == 'tgl':
            if cmd[1] in reg.keys():
                tgl = reg[cmd[1]]
            elif int(cmd[1]):
                tgl = int(cmd[1])

            if 0 <= (i + tgl) < len(instructions):
                cmd2 = instructions[i + tgl].split()
                if cmd2[0] == 'inc':
                    cmd2[0] = 'dec'
                elif cmd2[0] == 'dec':
                    cmd2[0] = 'inc'
                elif cmd2[0] == 'tgl':
                    cmd2[0] = 'inc'
                elif cmd2[0] == 'cpy':
                    cmd2[0] = 'jnz'
                elif cmd2[0] == 'jnz':
                    cmd2[0] = 'cpy'
                instructions[i + tgl] = ' '.join(cmd2)

        i += 1
        #print(cmd, reg)
        #print(instructions, i)

    return reg['a']


test = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""
assert run_instructions(test.split('\n')) == 3
print(run_instructions(open('23_input').read().split('\n'), a=7))