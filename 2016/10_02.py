"""advent of code 2016 day 10 part 1"""

class Bot(object):
    """class to store bot data"""
    def __init__(self, b_id):
        self.id = b_id
        self.low = -1
        self.high = -1
        self.rules = {}

    def add_chip(self, val):
        """set chip value based on value passed in"""
        if self.low != -1 and self.high != -1:
            print("error both taken")
        elif self.low == -1 and self.high == -1:
            self.low = val
        elif val >= self.low:
            self.high = val
        elif val < self.low:
            self.high = self.low
            self.low = val
        else:
            print("error uncaught")

    def add_rules(self, r):
        """add rules for the low or high chip"""
        if 'high' in r.keys() and 'low' in r.keys():
            self.rules = r
        else:
            print('bad rules')

    def has_two(self):
        """check if has two chips"""
        return self.low != -1 and self.high != -1


def print_bots(all_bots):
    """print all bots and their info"""
    print('id\tlow\thigh')
    for k, b in all_bots.items():
        assert k == b.id
        print(b.id, end="\t")
        print(b.low, end="\t")
        print(b.high, end="\t")
        print(b.rules['low'], end="\t")
        print(b.rules['high'], end="\t")
        print()



# data = open('testinput').read().splitlines()
data = open('input').read().splitlines()

bots = {}

for d in data:
    cmd = d.split()
    if cmd[0] == 'value':
        bot_id = int(cmd[-1])
        chip = int(cmd[1])
        # if bot already exists add the chip
        if bot_id in bots:
            bots[bot_id].add_chip(chip)
        else:
            bots[bot_id] = Bot(bot_id)
            bots[bot_id].add_chip(chip)

    elif cmd[0] == 'bot':
        bot_id = int(cmd[1])
        rules = {}
        rules['low'] = (cmd[5], int(cmd[6]))
        rules['high'] = (cmd[10], int(cmd[11]))
        if bot_id in bots:
            bots[bot_id].add_rules(rules)
        else:
            bots[bot_id] = Bot(bot_id)
            bots[bot_id].add_rules(rules)

# print_bots(bots)

output = {}

while True:
    found = False
    for k, b in bots.items():
        if b.has_two():
            found = True
            # execute low rule
            if b.rules['low'][0] == 'output':
                output_id = b.rules['low'][1]
                if output_id in output:
                    output[output_id].append(b.low)
                else:
                    output[output_id] = [b.low]
                b.low = -1
            else:
                bot_id = b.rules['low'][1]
                if bot_id in bots:
                    bots[bot_id].add_chip(b.low)
                    b.low = -1
                else:
                    print('bot not found')


            # execute high rule
            if b.rules['high'][0] == 'output':
                output_id = b.rules['high'][1]
                if output_id in output:
                    output[output_id].append(b.high)
                else:
                    output[output_id] = [b.high]
                b.high = -1
            else:
                bot_id = b.rules['high'][1]
                if bot_id in bots:
                    bots[bot_id].add_chip(b.high)
                    b.high = -1
                else:
                    print('bot not found')

    if not found:
        break

# print_bots(bots)
print(output[0][0] * output[1][0] * output[2][0])

