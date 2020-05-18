"""
Day 7 part 2

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
from copy import copy
from utils import read_integers


class IntCode:
    num_params = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}

    def __init__(self, data):
        self.data = data
        self.idx = 0
        self.input_idx = 0
        self.inpt = []
        self.output = []

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

        self.inpt += inpt

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
                    self.data[self.data[self.idx + 1]] = self.inpt[self.input_idx]
                    self.input_idx += 1
                    self.idx += 2
                elif op == 4:
                    self.output.append(params[0])
                    self.idx += 2
                    return self.output[-1], 1
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

        return self.output[-1], -1


def run_thrusters(data, phases):
    "run the thrusters"
    res = 0
    amps = []
    for p in phases:
        amps.append(IntCode(copy(data)))
        res, _ = amps[-1].run_program([p, res])

    # for each of the amplifiers
    done = False
    while not done:
        for i, _ in enumerate(amps):
            res, code = amps[i].run_program([res])
            if code == -1:
                done = True

    return res


def try_all_phases(data):
    "run all combos"
    phases = permutations((9, 8, 7, 6, 5))
    max_output = 0
    # for all permutations find max
    for p in phases:
        res = run_thrusters(data, p)
        if res > max_output:
            max_output = res
    return max_output


test_programs = [
    [
        3,
        26,
        1001,
        26,
        -4,
        26,
        3,
        27,
        1002,
        27,
        2,
        27,
        1,
        27,
        26,
        27,
        4,
        27,
        1001,
        28,
        -1,
        28,
        1005,
        28,
        6,
        99,
        0,
        0,
        5,
    ],
    [
        3,
        52,
        1001,
        52,
        -5,
        52,
        3,
        53,
        1,
        52,
        56,
        54,
        1007,
        54,
        5,
        55,
        1005,
        55,
        26,
        1001,
        54,
        -5,
        54,
        1105,
        1,
        12,
        1,
        53,
        54,
        53,
        1008,
        54,
        0,
        55,
        1001,
        55,
        1,
        55,
        2,
        53,
        55,
        53,
        4,
        53,
        1001,
        56,
        -1,
        56,
        1005,
        56,
        6,
        99,
        0,
        0,
        0,
        0,
        10,
    ],
]


assert try_all_phases(test_programs[0]) == 139629729
assert try_all_phases(test_programs[1]) == 18216


inpt = read_integers(7)

assert try_all_phases(inpt) == 6489132
