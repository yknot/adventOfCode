"""
Day 1 part 2
"""
from utils import read_input


test_inpt = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

digits = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def calibrate(vals):
    total = 0
    for val in vals:
        numbers = []
        for i, l in enumerate(val):
            if l.isdigit():
                numbers.append((i, l))

        for k, v in digits.items():
            start = 0
            while (loc := val.find(k, start)) != -1:
                numbers.append((loc, v))
                start = loc + 1

        numbers.sort(key=lambda x: x[0])
        total += int(numbers[0][1] + numbers[-1][1])

    return total


inpt = list(read_input(1))

assert calibrate(test_inpt) == 281

assert calibrate(inpt) == 56324
