import hashlib
import copy

def hash_dirs(hashable):
    dirs = hashlib.md5(hashable.encode()).hexdigest()[:4]
    valid = ['b', 'c', 'd', 'e', 'f']
    return (dirs[0] in valid, dirs[1] in valid,
            dirs[2] in valid, dirs[3] in valid)


class Maze(object):
    def __init__(self, code):
        start_config = {
            'x': 0,
            'y': 0,
            'code': code,
            'path': []
        }
        self.moves = [start_config]
        self.longest = 0

    def run(self):
        while self.moves:
            self.move()

        return self.longest

    def move(self):
        # take the next move
        m = self.moves.pop(0)

        # get directions
        up, down, left, right = hash_dirs(m['code'] + ''.join(m['path']))

        if m['x'] < 3 and right:
            m_new = copy.deepcopy(m)
            m_new['path'].append('R')
            m_new['x'] += 1
            if m_new['x'] == 3 and m_new['y'] == 3:
                self.longest = max(self.longest, len(m_new['path']))
            else:
                self.moves.append(m_new)
        if m['y'] < 3 and down:
            m_new = copy.deepcopy(m)
            m_new['path'].append('D')
            m_new['y'] += 1
            if m_new['x'] == 3 and m_new['y'] == 3:
                self.longest = max(self.longest, len(m_new['path']))
            else:
                self.moves.append(m_new)
        if m['x'] > 0 and left:
            m_new = copy.deepcopy(m)
            m_new['path'].append('L')
            m_new['x'] -= 1
            if m_new['x'] == 3 and m_new['y'] == 3:
                self.longest = max(self.longest, len(m_new['path']))
            else:
                self.moves.append(m_new)
        if m['y'] > 0 and up:
            m_new = copy.deepcopy(m)
            m_new['path'].append('U')
            m_new['y'] -= 1
            if m_new['x'] == 3 and m_new['y'] == 3:
                self.longest = max(self.longest, len(m_new['path']))
            else:
                self.moves.append(m_new)


# test
assert Maze('ihgpwlah').run() == 370
assert Maze('kglvqrro').run() == 492
assert Maze('ulqzkmiv').run() == 830

print(Maze('pslxynzg').run())