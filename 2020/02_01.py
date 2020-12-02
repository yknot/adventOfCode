"""
Day 2
"""

from utils import read_input


def check_valid(pwds):
    valid = 0
    for rng, letter, pwd in pwds:
        lo, hi = [int(x) for x in rng.split("-")]
        letter = letter[0]

        n = pwd.count(letter)
        if n >= lo and n <= hi:
            valid += 1

    return valid


inpt = read_input(2, line_parser=str.split)

assert check_valid(inpt) == 493
