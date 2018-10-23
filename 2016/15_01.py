def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)

class DiscStack(object):
    def __init__(self, config):
        """read in the config"""
        self.discs = []
        for i, c in enumerate(config):
            tok = c.split()
            total = int(tok[3])
            start = int(tok[-1].strip('.'))
            div = total - (i + 1 + start) % total
            self.discs.append((total, start, div))

    def find_min_time(self):
        """find the minimum time where the capsule would fall through"""
        time = 0
        inc = 1
        while True:
            for i, d in enumerate(self.discs):
                if (time + i + 1 + d[1]) % d[0] != 0:
                    break
                else:
                    inc = lcm(inc, d[0])
            else:
                break

            time += inc

        return time


testinput = ['Disc #1 has 5 positions; at time=0, it is at position 4.',
             'Disc #2 has 2 positions; at time=0, it is at position 1.']

ds = DiscStack(testinput)
assert ds.find_min_time() == 5

realinput = open('input').read().split('\n')
ds = DiscStack(realinput)
assert ds.find_min_time() == 376777
