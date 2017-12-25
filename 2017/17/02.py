def run_inserts(steps):
    """run 2017 inserts"""
    spot = 0
    final = 0
    for i in range(1, 50000000):
        spot = (steps + spot) % i
        spot += 1
        if spot == 1:
            final = i

    return final


# test_steps = 3
# assert run_inserts(test_steps) == 638

final_steps = 377
print(run_inserts(final_steps))
