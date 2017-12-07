def redistribute(banks, states):
    """redistribute memory across banks"""
    loops = 1
    while True:
        # get largest bank
        largest = min([k for k, v in banks.items()
                       if v == max(banks.values())])

        # grab the memory to redistribute and reset
        redis = banks[largest]
        banks[largest] = 0

        # redistribute
        idx = largest
        length = max(banks.keys())
        while redis > 0:
            # if at end wrap
            if idx == length:
                idx = 0
            else:
                idx += 1
            banks[idx] += 1
            redis -= 1

        # check if exists in set
        state = hash(frozenset(banks.items()))
        if state in states:
            return loops - states[state]
        states[state] = loops
        loops += 1


example = {i: j for i, j in enumerate([0, 2, 7, 0])}
states = {}
states[hash(frozenset(example.items()))] = 0

assert redistribute(example, states) == 4

validation = {i: j for i, j in enumerate([10, 3, 15, 10, 5, 15,
                                          5, 15, 9, 2, 5, 8, 5,
                                          2, 3, 6])}
states = {}
states[hash(frozenset(validation.items()))] = 0

print(redistribute(validation, states))
