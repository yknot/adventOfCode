"""
Day 1
"""
from utils import read_input


test_inpt = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]


def calibrate(vals):
    total = 0
    for v in vals:
        numbers = []
        for l in v:
            if l.isdigit():
                numbers.append(l)

        total += int(numbers[0] + numbers[-1])

    return total


inpt = list(read_input(1))

assert calibrate(test_inpt) == 142

assert calibrate(inpt) == 55108
