from collections import defaultdict
import operator
ops = {
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt
}


def run_comparison(a, op, b):
    """run the operation"""
    operation = ops.get(op)
    return operation(a, b)


def parse_data(data):
    """read in the raw data and parse into commands"""
    regs = defaultdict(int)
    maximum = 0

    # for each command
    for d in data:
        # split data
        change, cmd, amount, _, cmp_var, op, cmp_amt = d.split()

        # if the condition is true
        if run_comparison(regs[cmp_var], op, int(cmp_amt)):
            # check inc vs dec
            if cmd == 'inc':
                regs[change] += int(amount)
            else:
                regs[change] -= int(amount)

        # find maximum ever
        tmp_max = max(regs.values())
        if tmp_max > maximum:
            maximum = tmp_max

    # return max register value
    return maximum


test_data = open('testinput').read().splitlines()
assert parse_data(test_data) == 10

test_data = open('input').read().splitlines()
print(parse_data(test_data))
