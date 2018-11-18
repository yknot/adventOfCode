reg = {'a': 12, 'b': 0, 'c': 0, 'd': 0}

# cpy a b
reg['b'] = reg['a']
# dec b
reg['b'] -= 1

while 1:
    # cpy a d
    reg['d'] = reg['a']
    # cpy 0 a
    reg['a'] = 0
    # cpy b c
    reg['c'] = reg['b']

    reg['a'] += (reg['c'] * reg['d'])
    reg['c'] = 0
    reg['d'] = 0

    # dec b
    reg['b'] -= 1
    # cpy b c
    reg['c'] = reg['b']
    # cpy c d
    reg['d'] = reg['c']

    reg['c'] += reg['d']
    reg['d'] = 0

    if reg['c'] == 2:
        break

    reg['c'] = -16
reg['a'] += (80 * 73)
reg['c'] = 0
reg['d'] = 0

assert reg['a'] == 479007440
assert reg['b'] == 1
assert reg['c'] == 0
assert reg['d'] == 0
print(reg)