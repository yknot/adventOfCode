def run_inserts(steps):
    """run 2017 inserts"""
    lock = [0]
    spot = 0
    for i in range(1, 2018):
        spot = (steps + spot) % i
        spot += 1
        lock.insert(spot, i)

    return lock[lock.index(2017) + 1]


test_steps = 3
assert run_inserts(test_steps) == 638

final_steps = 377
print(run_inserts(final_steps))
