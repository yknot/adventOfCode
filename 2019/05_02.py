"""
Day 5 part 2

continuation of the program from day 2
adds new instructions
    3 takes in input and stores at the position indicated by first param
    4 outputs the value stored at first param
    5 jump if true, if first param non-zero jump to second param
    6 jump if false if first param zero jump to second param
    7 less than if first param is less than second store 1 in third param else store 0
    8 equals if first para equals second store 1 in third param else store 0
orig instructions
    1 adds values from positions after 1 and stores in third position
    2 multiplies in the same way
    
parameter modes
    0 indicates parameter mode
    1 indicates immediate mode



two digit op code in the ones and tens column
follows for each mode of parameter leading 0s omitted

"""

from utils import read_integers, ints


class IntCode:
    num_params = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}

    def __init__(self, inpt):
        self.data = inpt
        self.idx = 0

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
                    self.data[self.data[self.idx + 1]] = inpt
                elif op == 4:
                    out = params[0]
                    output.append(out)
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
                    self.data[self.data[self.idx + 3]] = (
                        1 if params[0] < params[1] else 0
                    )
                elif op == 8:
                    self.data[self.data[self.idx + 3]] = (
                        1 if params[0] == params[1] else 0
                    )
                self.idx += 4
        return output


assert IntCode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]).run_program(8)[-1] == 1
assert IntCode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]).run_program(7)[-1] == 0

assert IntCode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]).run_program(8)[-1] == 0
assert IntCode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]).run_program(5)[-1] == 1


assert (
    IntCode([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]).run_program(0)[
        -1
    ]
    == 0
)
assert (
    IntCode([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]).run_program(1)[
        -1
    ]
    == 1
)
assert (
    IntCode([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]).run_program(0)[-1] == 0
)
assert (
    IntCode([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]).run_program(1)[-1] == 1
)

for i in range(5, 11):
    assert (
        IntCode(
            [
                3,
                21,
                1008,
                21,
                8,
                20,
                1005,
                20,
                22,
                107,
                8,
                21,
                20,
                1006,
                20,
                31,
                1106,
                0,
                36,
                98,
                0,
                0,
                1002,
                21,
                125,
                20,
                4,
                20,
                1105,
                1,
                46,
                104,
                999,
                1105,
                1,
                46,
                1101,
                1000,
                1,
                20,
                4,
                20,
                1105,
                1,
                46,
                98,
                99,
            ]
        ).run_program(i)[-1]
        == 999
        if i < 8
        else 1000
        if i == 8
        else 1001
    )

inpt = read_integers(5)
res = IntCode(inpt).run_program(5)

assert all([i == 0 for i in res[:-1]])
assert res[-1] == 4655956
