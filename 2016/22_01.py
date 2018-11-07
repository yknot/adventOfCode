"""Day 22 part 1"""


class Drive():
    """class to define a drive"""

    def __init__(self, x, y, size, used, avail):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = avail

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
        drives.append(Drive(x, y, size, used, avail))

    return drives


def get_pairs(drives):
    """get pairs of drives"""
    pairs = 0
    for i, a in enumerate(drives):
        # cannot have A be 0
        if a.used == 0:
            continue
        for j, b in enumerate(drives):
            # A cannot equal B
            if i == j:
                continue

            # A used less than or equal to B avail
            if a.used <= b.avail:
                pairs += 1
            else:
                break

    return pairs


drive_list = parse_drives(open('22_input').read().splitlines())
drive_list = sorted(drive_list, reverse=True)
print(get_pairs(drive_list))
