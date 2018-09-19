class DiscStack(object):
    def __init__(self, config):
        """read in the config"""
        self.discs = []
        for c in config:
            tok = c.split()
            total = int(tok[3])
            start = int(tok[-1].strip('.'))
            self.discs.append((total, start))

    def find_min_time(self):
        """find the minimum time where the capsule would fall through"""
        time = 0
        while True:
            passed = True
            for i, d in enumerate(self.discs):
                if (time + i + 1 + d[1]) % d[0] != 0:
                    passed = False
                    break

            if passed:
                break

            time += 1

        return time


testinput = ['Disc #1 has 5 positions; at time=0, it is at position 4.',
             'Disc #2 has 2 positions; at time=0, it is at position 1.']

ds = DiscStack(testinput)
assert ds.find_min_time() == 5

realinput = open('input').read().split('\n')
ds = DiscStack(realinput)
print(ds.find_min_time())
