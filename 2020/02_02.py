"""
Day 2
"""

from utils import read_input
from operator import xor


def check_valid(pwds):
    valid = 0
    for rng, letter, pwd in pwds:
        lo, hi = [int(x) - 1 for x in rng.split("-")]
        letter = letter[0]

        if xor(pwd[lo] == letter, pwd[hi] == letter):
            valid += 1

    return valid


inpt = read_input(2, line_parser=str.split)


assert check_valid(inpt) == 593
