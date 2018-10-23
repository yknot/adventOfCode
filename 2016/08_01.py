"""advent of code 2016 day 8 part 1"""

# data = ['rect 3x2',
#         'rotate column x=1 by 1',
#         'rotate row y=0 by 4',
#         'rotate column x=1 by 1']

# x = 7
# y = 3

data = open('input').read().splitlines()
x = 50
y = 6

# create empty board
board = [['.'] * x for _ in range(y)]


def make_rect(shape, b):
    """make a rectangle in upper right corner"""
    x_len = int(shape.split('x')[0])
    y_len = int(shape.split('x')[1])

    for i in range(y_len):
        for j in range(x_len):
            b[i][j] = '#'
    return b


def rot_col(c, num, b):
    """rotate column c by param num"""
    c = int(c.split('=')[1])
    for _ in range(num):
        prev = ''
        for line in b:
            tmp = line[c]
            if prev != '':
                line[c] = prev
            prev = tmp
        b[0][c] = prev
    return b


def rot_row(r, num, b):
    """rotate row r by param num"""
    r = int(r.split('=')[1])
    for _ in range(num):
        prev = ''
        for i in range(len(b[r])):
            tmp = b[r][i]
            if prev != '':
                b[r][i] = prev
            prev = tmp
        b[r][0] = prev
    return b


for d in data:
    cmd = d.split()[0]
    if cmd == 'rect':
        board = make_rect(d.split()[1], board)
    elif cmd == 'rotate':
        direction = d.split()[1]
        if direction == 'column':
            rot_col(d.split()[2], int(d.split()[4]), board)
        elif direction == 'row':
            rot_row(d.split()[2], int(d.split()[4]), board)

    print('\n'.join([''.join(b) for b in board]))
    print()

print((''.join(''.join(b) for b in board)).count('#'))
