from dataclasses import dataclass
from math import prod

example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


@dataclass
class Problem:
    num_list: list[int]
    op: str = None

    @property
    def result(self) -> int:
        if self.op == "*":
            return prod(self.num_list)
        elif self.op == "+":
            return sum(self.num_list)
        else:
            raise Exception("op not valid")


@dataclass
class Worksheet:
    problems: list[Problem]

    def calc_worksheet(self) -> int:
        return sum([prob.result for prob in self.problems])


def parse(inpt: str) -> Worksheet:
    lines = inpt.split("\n")

    problems = [Problem([int(val)]) for val in lines[0].split()]

    for line in lines[1:-1]:
        for prob, val in zip(problems, line.split()):
            prob.num_list.append(int(val))

    for prob, op in zip(problems, lines[-1].split()):
        prob.op = op

    return Worksheet(problems)


def parse_by_column(inpt: str) -> Worksheet:
    lines = inpt.split("\n")

    problems = []
    num_list = []
    num = []
    skip = False

    for col_idx in range(len(lines[0]) - 1, -1, -1):
        if skip:
            skip = False
            continue
        for row_idx in range(0, len(lines) - 1):
            num.append(lines[row_idx][col_idx])
        num_list.append(int("".join(num)))
        num = []
        if lines[-1][col_idx] in ["+", "*"]:
            problems.append(Problem(num_list, lines[-1][col_idx]))
            num_list = []
            skip = True

    return Worksheet(problems)


def run_worksheet(inpt: str, column_parse: bool = False) -> int:
    if column_parse:
        return parse_by_column(inpt).calc_worksheet()
    return parse(inpt).calc_worksheet()


with open("06_input") as f:
    data = f.read()


assert run_worksheet(example) == 4277556
assert run_worksheet(data) == 3785892992137

assert run_worksheet(example, column_parse=True) == 3263827
assert run_worksheet(data, column_parse=True) == 7669802156452
