"""
Day 1
"""
from utils import read_input


test_inpt = [
    "1000",
    "2000",
    "3000",
    "",
    "4000",
    "",
    "5000",
    "6000",
    "",
    "7000",
    "8000",
    "9000",
    "",
    "10000",
]


def top_three_elves(vals):
    elves = []
    cur_sum = 0
    for line in vals:
        if line:
            cur_sum += int(line)
        else:
            elves.append(cur_sum)
            cur_sum = 0

    elves.append(cur_sum)

    return sum(sorted(elves)[-3:])


inpt = list(read_input(1))

assert top_three_elves(test_inpt) == 45000

assert top_three_elves(inpt) == 207148
