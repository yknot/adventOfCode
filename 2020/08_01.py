"""
Day 8 part 1
"""

from utils import read_input


def break_loop(instructions):

    accumulator = 0
    idx = 0

    visited = set()

    while True:
        op, num = instructions[idx]
        if idx in visited:
            break

        visited.add(idx)
        # acc increase by value
        if op == "acc":
            accumulator += num
            idx += 1
        # jmp jump forward n instructions
        elif op == "jmp":
            idx += num
        # nop no operation
        elif op == "nop":
            idx += 1

    return accumulator


def parser(line):
    op, num = line.split()
    return (op, int(num))


test_inpt = read_input(8, file_template="{:02}_test_input", line_parser=parser)
assert break_loop(test_inpt) == 5

inpt = read_input(8, line_parser=parser)
assert break_loop(inpt) == 1941
