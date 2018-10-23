import numpy as np


def read_data(filename):
    """read in the components"""
    return [tuple([int(e) for e in l.split('/')])
            for l in open(filename).read().splitlines()]


def next_step(components, bridge, next_val):
    nexts = [c for c in components if c not in bridge and next_val in c]
    # base case no next step
    if not len(nexts):
        return np.sum(bridge)
    max_val = 0
    for n in nexts:
        next_val_next = n[0] if n[1] == next_val else n[1]
        bridge.append(n)
        res = next_step(components, bridge, next_val_next)
        if res > max_val:
            max_val = res
        bridge.pop(-1)
    return max_val


def run_algo(components):
    """find the strongest bridge"""
    max_bridge_str = 0
    starts = [c for c in components if 0 in c]
    # for all possible bridge starts
    for s in starts:
        # intial state
        bridge = [s]
        next_val = s[0] if s[1] == 0 else s[1]
        res = next_step(components, bridge, next_val)
        if res > max_bridge_str:
            max_bridge_str = res
    return max_bridge_str


assert run_algo(read_data('testinput')) == 31
print('Passed testinput')
print(run_algo(read_data('input')))
