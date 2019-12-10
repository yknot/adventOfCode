"""
Day 2 part 2

Intcode program is a list of ints separated by commas
opcodes
    1 adds values from positions after 1 and stores in third position
    2 multiplies in the same way
after opcode move forward 4

terms
    instruction pointer -> idx
    parameters -> vals used
    increment by length of parameters
    
output:
what pair of inputs produces 19690720
    between 0 and 99
    inpt[1] -> noun
    inpt[2] -> verb

"""
import copy
from utils import read_integers


def run_ops(inpt):
    idx = 0
    while idx < len(inpt):
        if inpt[idx] == 1:
            # run addition
            inpt[inpt[idx + 3]] = inpt[inpt[idx + 1]] + inpt[inpt[idx + 2]]
            idx += 4
        elif inpt[idx] == 2:
            # run multiplication
            inpt[inpt[idx + 3]] = inpt[inpt[idx + 1]] * inpt[inpt[idx + 2]]
            idx += 4
        elif inpt[idx] == 99:
            # halt
            break
        else:
            # print("ERROR")
            return [0]

    return inpt


def run_all(inpt):
    while 1:
        for noun in range(100):
            for verb in range(100):
                data = list(copy.copy(inpt))
                data[1] = noun
                data[2] = verb

                if run_ops(data)[0] == 19690720:
                    return 100 * noun + verb


# run tests
def tests():
    assert run_ops([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run_ops([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert run_ops([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert run_ops([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


tests()


# swap out first two
assert run_all(read_integers(2)) == 7195
