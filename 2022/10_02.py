"""
Day 10
"""
from utils import read_input


def compute_power(inpt):
    board = []
    line = []

    power = 1
    for x, n in inpt:
        # if at the end of the line
        if len(line) == 40:
            board.append(line)
            line = []

        if x == "noop":
            if power - 1 <= len(line) <= power + 1:
                line.append("#")
            else:
                line.append(".")
        elif x == "addx":
            if power - 1 <= len(line) <= power + 1:
                line.append("#")
            else:
                line.append(".")

            if len(line) == 40:
                board.append(line)
                line = []

            if power - 1 <= len(line) <= power + 1:
                line.append("#")
            else:
                line.append(".")
            power += n

    board.append(line)
    # for l in board:
    #     print("".join(l))
    # print()


def parser(line):
    if line.strip() == "noop":
        return ("noop", None)
    x, n = line.split()
    return (x, int(n))


test_inpt = read_input(10, line_parser=parser, file_template="{:02}_test_input")
compute_power(test_inpt)

inpt = read_input(10, line_parser=parser)
compute_power(inpt)
