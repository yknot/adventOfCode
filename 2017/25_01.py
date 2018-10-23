def run_algo(data):
    """using the data run the algorithm"""
    loc = 0
    state = data['state']
    ones = set()
    for i in range(data['tot_steps']):
        # value is 1 at location
        if loc in ones:
            write, move, cont = data[state][1]
            if not write:
                ones.remove(loc)

        # else it is 0
        else:
            write, move, cont = data[state][0]
            if write:
                ones.add(loc)

        loc += move
        state = cont

    return len(ones)


def parse(raw):
    """parse the input"""
    data = {}
    i = 0
    while i < len(raw):
        if raw[i].startswith('Begin in state'):
            # get start state
            data['state'] = raw[i].split(' ')[-1].strip('.')
        elif raw[i].startswith('Perform a diagnostic checksum after'):
            # get end state
            data['tot_steps'] = int(raw[i].split(' ')[-2])
        elif raw[i].startswith('In state'):
            # parse state rules
            state = raw[i].split(' ')[-1].strip(':')
            state_data = {}
            i += 1
            while i < len(raw) and raw[i] != '':
                value = int(raw[i].split(' ')[-1].strip(':'))
                write = int(raw[i + 1].split(' ')[-1].strip('.'))
                move = raw[i + 2].split(' ')[-1].strip('.')
                move = 1 if move == 'right' else -1
                cont = raw[i + 3].split(' ')[-1].strip('.')
                state_data[value] = [write, move, cont]
                i += 4

            data[state] = state_data

        i += 1

    return data


test_raw = open('testinput').read().splitlines()
data = parse(test_raw)
assert run_algo(data) == 3

raw = open('input').read().splitlines()
data = parse(raw)
print(run_algo(data))
