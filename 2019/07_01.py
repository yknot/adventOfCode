"""
Day 7

continuation of the program from day 2

instructions
    1 adds values from positions after 1 and stores in third position
    2 multiplies in the same way
    3 takes in input and stores at the position indicated by first param
    4 outputs the value stored at first param

parameter modes
    0 indicates parameter mode
    1 indicates immediate mode



two digit op code in the ones and tens column
follows for each mode of parameter leading 0s omitted

"""

from itertools import permutations
from utils import read_integers


class IntCode:
    num_params = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}

    def __init__(self, inpt):
        self.data = inpt
        self.idx = 0
        self.input_idx = 0

    def parse_cmd(self):
        "parse the command"
        str_cmd = str(self.data[self.idx]).zfill(5)

        op = int(str_cmd[-2:])

        # get the right number of params and flip
        param_modes = list(str_cmd)[3 - self.num_params[op] : 3][::-1]

        params = []
        for i, p in enumerate(param_modes):
            if p == "1":
                params.append(self.data[self.idx + 1 + i])
            elif p == "0":
                params.append(self.data[self.data[self.idx + 1 + i]])

        return op, params

    def run_program(self, inpt):
        "run the calculations"

        output = []

        while self.data[self.idx] != 99:
            op, params = self.parse_cmd()
            if op in [1, 2]:
                if op == 1:
                    self.data[self.data[self.idx + 3]] = params[0] + params[1]
                elif op == 2:
                    self.data[self.data[self.idx + 3]] = params[0] * params[1]
                self.idx += 4
            elif op in [3, 4]:
                if op == 3:
                    self.data[self.data[self.idx + 1]] = inpt[self.input_idx]
                    self.input_idx += 1
                elif op == 4:
                    output.append(params[0])
                self.idx += 2
            elif op in [5, 6]:
                if op == 5 and params[0] != 0:
                    self.idx = params[1]
                elif op == 6 and params[0] == 0:
                    self.idx = params[1]
                else:
                    self.idx += 3
            elif op in [7, 8]:
                if op == 7:
                    self.data[self.data[self.idx + 3]] = int(params[0] < params[1])
                elif op == 8:
                    self.data[self.data[self.idx + 3]] = int(params[0] == params[1])
                self.idx += 4
        return output


def run_thrusters(data, amps):
    "run the thrusters"
    res = 0
    # for each of the amplifiers
    for a in amps:
        res = IntCode(data).run_program([a, res])[0]
    return res


def try_all_phases(data):
    "run all combos"
    phases = permutations((4, 3, 2, 1, 0))
    max_output = 0
    # for all permutations find max
    for p in phases:
        res = run_thrusters(data, p)
        if res > max_output:
            max_output = res
    return max_output


test_programs = [
    [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
    [
        3,
        23,
        3,
        24,
        1002,
        24,
        10,
        24,
        1002,
        23,
        -1,
        23,
        101,
        5,
        23,
        23,
        1,
        24,
        23,
        23,
        4,
        23,
        99,
        0,
        0,
    ],
    [
        3,
        31,
        3,
        32,
        1002,
        32,
        10,
        32,
        1001,
        31,
        -2,
        31,
        1007,
        31,
        0,
        33,
        1002,
        33,
        7,
        33,
        1,
        33,
        31,
        31,
        1,
        32,
        31,
        31,
        4,
        31,
        99,
        0,
        0,
        0,
    ],
]


assert try_all_phases(test_programs[0]) == 43210
assert try_all_phases(test_programs[1]) == 54321
assert try_all_phases(test_programs[2]) == 65210


inpt = read_integers(7)

assert try_all_phases(inpt) == 14902
