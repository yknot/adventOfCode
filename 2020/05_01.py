"""
Day 5
"""

from utils import read_input


def find_seat(tickets):
    max_ticket = 0
    for t in tickets:
        row_dir = t[:7]
        lo, hi = 0, 127
        for r in row_dir:
            if r == "F":
                hi = ((hi - lo) // 2) + lo
            else:
                lo = ((hi - lo) // 2) + lo

        row = hi

        col_dir = t[7:]
        lo, hi = 0, 7
        for r in col_dir:
            if r == "L":
                hi = ((hi - lo) // 2) + lo
            else:
                lo = ((hi - lo) // 2) + lo

        col = hi

        val = (row * 8) + col
        if val > max_ticket:
            max_ticket = val

    return max_ticket


test_input = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

assert find_seat(test_input) == 820

inpt = read_input(5)

assert find_seat(inpt) == 922
