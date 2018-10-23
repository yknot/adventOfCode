class FireWall(object):
    def __init__(self, config):
        """initial config"""
        self.depths = eval('{' + config.replace('\n', ',') + '}')
        self.positions = {k: 1 for k, v in self.depths.items()}
        self.direction = {k: 'up' for k, v in self.depths.items()}
        self.caught = []

    def run(self):
        """run the simulation"""
        pos = 0
        while pos <= max(self.depths.keys()):
            # check if caught
            if pos in self.positions and self.positions[pos] == 1:
                self.caught.append(pos)

            # increment positions
            for k in self.positions.keys():
                if self.direction[k] == 'up':
                    self.positions[k] += 1
                    if self.positions[k] == self.depths[k]:
                        self.direction[k] = 'down'
                else:
                    self.positions[k] -= 1
                    if self.positions[k] == 1:
                        self.direction[k] = 'up'

            # increment pos
            pos += 1

    def calc_severity(self):
        """calculate the severity"""
        return sum([k * self.depths[k] for k in self.caught])


fw_test = FireWall(open('testinput').read())
fw_test.run()
assert fw_test.calc_severity() == 24


fw = FireWall(open('input').read())
fw.run()
print(fw.calc_severity())
