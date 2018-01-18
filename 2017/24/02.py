def read_data(filename):
    """read in the components"""
    return [tuple([int(e) for e in l.split('/')])
            for l in open(filename).read().splitlines()]


def next_step(components, bridge, next_val):
    nexts = [c for c in components if next_val in c and c not in bridge]
    # base case no next step
    if not len(nexts):
        return len(bridge), sum(map(sum, bridge))
    max_val = max_len = 0
    for n in nexts:
        next_val_next = n[0] if n[1] == next_val else n[1]
        bridge.add(n)
        res_len, res_val = next_step(components, bridge, next_val_next)
        if res_len > max_len:
            max_len = res_len
            max_val = res_val
        elif res_len == max_len and res_val > max_val:
            max_val = res_val
        bridge.remove(n)
    return max_len, max_val


def run_algo(components):
    """find the strongest bridge"""
    max_val = max_len = 0
    starts = [c for c in components if 0 in c]
    # for all possible bridge starts
    for s in starts:
        # intial state
        bridge = set()
        bridge.add(s)
        next_val = s[0] if s[1] == 0 else s[1]
        res_len, res_val = next_step(components, bridge, next_val)
        if res_len > max_len:
            max_len = res_len
            max_val = res_val
        elif res_len == max_len and res_val > max_val:
            max_val = res_val

    return max_val


assert run_algo(read_data('testinput')) == 19
print('Passed testinput')
print(run_algo(read_data('input')))
