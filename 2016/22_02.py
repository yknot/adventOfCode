"""Day 22 part 2"""


class Drive():
    """class to define a drive"""

    def __init__(self, x, y, size, used, avail):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = avail
        self.too_big = False
        self.target = False

    def __repr__(self):
        if self.too_big:
            return '(#####)'
        if self.target:
            return f'*{self.used}/{self.size}*'
        if self.used == 0:
            return f'(___{self.size})'
        # return f'({self.x}, {self.y})'
        return f'({self.used}/{self.size})'

    def __lt__(self, other):
        return self.avail < other.avail


def parse_drives(lines):
    """parse the text of drives"""
    drives = []
    for l in lines:
        tok = l.split()
        _, x, y = tok[0].split('-')
        x = int(x.strip('x'))
        y = int(y.strip('y'))
        size = int(tok[1].strip('T'))
        used = int(tok[2].strip('T'))
        avail = int(tok[3].strip('T'))
        while len(drives) <= y:
            drives.append([])
        while len(drives[y]) <= x:
            drives[y].append(None)

        drives[y][x] = (Drive(x, y, size, used, avail))

    return drives


def mark_drives(drives):
    """mark large drives and target drive"""
    drives[0][-1].target = True
    for i, _ in enumerate(drives):
        for j, _ in enumerate(drives[i]):
            if drives[i][j].size > 100 and drives[i][j].used > 100:
                drives[i][j].too_big = True
            if drives[i][j].used == 0:
                y = i
                x = j

    return drives, (y, x)


def print_drives(drives):
    """pretty print function"""
    print('[')
    for i, _ in enumerate(drives):
        print('[', end='')
        for j, _ in enumerate(drives[i]):
            print(drives[i][j], end=', ')
        print(']')
    print(']')


drive_list = parse_drives(open('22_input').read().splitlines())
drive_list, empty = mark_drives(drive_list)
print_drives(drive_list)

# from visual inspection
#   move 34 columns over
#   move 27 columns up
#   move 34 columns over (swapping with the ** on the last move)
#   repeat the 5 step move 34 times to get the ** to the start
assert 34 + 27 + 34 + (5 * 34) == 265
