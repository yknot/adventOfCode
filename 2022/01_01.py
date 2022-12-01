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


def max_elf(vals):
    cur_sum = 0
    max_sum = 0
    for line in vals:
        if line:
            cur_sum += int(line)
        else:
            if cur_sum > max_sum:
                max_sum = cur_sum
            cur_sum = 0

    if cur_sum > max_sum:
        max_sum = cur_sum

    return max_sum


inpt = list(read_input(1))

assert max_elf(test_inpt) == 24000

assert max_elf(inpt) == 70720
