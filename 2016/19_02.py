"""day 19 part 2"""
import numpy as np


def run_algo(n):
    """run the full algo"""
    elves = np.array(list(range(1, n + 1)))
    # get first half point
    bot = len(elves) // 2
    # defines whether next spot is skipped
    skip = True if len(elves) % 2 == 1 else False

    while len(elves) > 1:
        mask = np.ones(len(elves), np.bool)
        # pattern is 2 False 1 True until you get to 1 number
        mask[range(bot, len(elves), 3)] = 0
        mask[range(bot + (2 if skip else 1), len(elves), 3)] = 0
        elves = elves[mask]

        # setup next loop by finding where we ended
        bot, skip = 0, False
        if not mask[-1] and not mask[-2]:
            bot = 1
        elif not mask[-1] and mask[-2]:
            skip = True

        # corner case where it will break
        if len(elves) == 2:
            if bot == 1:
                return elves[0]
            return elves[1]

    return elves[0]


# test cases and real test
assert run_algo(5) == 2
assert run_algo(10) == 1
assert run_algo(20) == 13
print(run_algo(3012210))
