"""
Day 5 part 2
"""

from utils import read_input


def find_seat(tickets):
    spots = []
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
        spots.append(val)

    spots = sorted(spots)
    lo, hi = spots[0], spots[-1]
    for idx, val in enumerate(range(lo, hi)):
        if spots[idx] != val:
            return val

    return -1


inpt = read_input(5)
assert find_seat(inpt) == 747
