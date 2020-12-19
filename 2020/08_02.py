"""
Day 8 part 2
"""

from utils import read_input


def break_loop(instructions):
    instruction_idx = 0

    while True:
        accumulator = 0
        idx = 0

        visited = set()

        while instructions[instruction_idx][0] not in ["nop", "jmp"]:
            instruction_idx += 1

        while idx != len(instructions):
            op, num = instructions[idx]

            if idx in visited:
                break

            visited.add(idx)

            if idx == instruction_idx:
                op = "jmp" if op == "nop" else "nop"
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

        if idx == len(instructions):
            return accumulator

        instruction_idx += 1

    return None


def parser(line):
    op, num = line.split()
    return (op, int(num))


test_inpt = read_input(8, file_template="{:02}_test_input", line_parser=parser)
assert break_loop(test_inpt) == 8

inpt = read_input(8, line_parser=parser)
assert break_loop(inpt) == 2096
