def redistribute(banks, states):
    """redistribute memory across banks"""
    iter = 1
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
            return iter
        states.add(state)
        iter += 1


example = {i: j for i, j in enumerate([0, 2, 7, 0])}
states = set()
states.add(hash(frozenset(example.items())))

assert redistribute(example, states) == 5

validation = {i: j for i, j in enumerate([10, 3, 15, 10, 5, 15,
                                          5, 15, 9, 2, 5, 8, 5,
                                          2, 3, 6])}
states = set()
states.add(hash(frozenset(validation.items())))

print(redistribute(validation, states))
