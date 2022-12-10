"""
Day 10
"""
from utils import read_input


def compute_power(inpt):
    stops = [20, 60, 100, 140, 180, 220]
    stop_vals = []

    i = 1
    power = 1
    j = 0
    for x, n in inpt:
        # if we perfectly line up
        if i == stops[j]:
            stop_vals.append(power)
            j += 1
            # quit the loop
            if j >= len(stops):
                break

        if x == "noop":
            i += 1
        elif x == "addx":
            if i + 1 == stops[j]:
                stop_vals.append(power)
                j += 1
                # quit the loop
                if j >= len(stops):
                    break

            i += 2
            power += n

    return sum([x * y for x, y in zip(stops, stop_vals)])


def parser(line):
    if line.strip() == "noop":
        return ("noop", None)
    x, n = line.split()
    return (x, int(n))


test_inpt = read_input(10, line_parser=parser, file_template="{:02}_test_input")
assert compute_power(test_inpt) == 13140

inpt = read_input(10, line_parser=parser)
assert compute_power(inpt) == 16020
