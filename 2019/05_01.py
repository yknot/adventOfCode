"""
Day 5

continuation of the program from day 2
adds new instructions
    3 takes in input and stores at the position indicated by first param
    4 outputs the value stored at first param
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


def parse_cmd(cmd):
    "parse the instruction and parameter modes"
    str_cmd = str(cmd).zfill(5)

    op = int(str_cmd[-2:])
    if op in [1, 2]:
        param_modes = list(str_cmd)[2::-1]
    elif op in [3, 4]:
        param_modes = str_cmd[2:3]

    return op, ints(param_modes)


def run_program(data, inpt):
    "run the program"

    output = []
    idx = 0
    # stopping condition
    while data[idx] != 99:
        o, pm = parse_cmd(data[idx])

        if o in [1, 2]:

            a = data[idx + 1] if pm[0] else data[data[idx + 1]]
            b = data[idx + 2] if pm[1] else data[data[idx + 2]]

            if o == 1:
                data[data[idx + 3]] = a + b
            elif o == 2:
                data[data[idx + 3]] = a * b

            idx += 4

        elif o in [3, 4]:

            if o == 3:
                data[data[idx + 1]] = inpt
            elif o == 4:
                out = data[idx + 1] if pm[0] else data[data[idx + 1]]
                output.append(out)

            idx += 2

    return output


test_programs = [[1002, 4, 3, 4, 33], [1101, 100, -1, 4, 0]]


for t in test_programs:
    run_program(t, 0)


inpt = read_integers(5)

res = run_program(inpt, 1)

assert all([i == 0 for i in res[:-1]])
assert res[-1] == 14522484
