from dataclasses import dataclass

example = """987654321111111
811111111111119
234234234234278
818181911112111"""


@dataclass
class ValPair:
    value: int
    index: int

    @property
    def value_str(self):
        return str(self.value)


@dataclass
class Bank:
    batteries: list[int]

    def find_max_joltage(self, length: int) -> int:
        max_vals: list[ValPair] = []

        while len(max_vals) < length:
            start = 0
            if max_vals:
                start = max_vals[-1].index + 1

            end = length - len(max_vals) - 1

            if end != 0:
                next_val = max(self.batteries[start:-end])
                next_index = self.batteries[start:].index(next_val) + start
            else:
                next_val = max(self.batteries[start:])
                next_index = self.batteries[start:].index(next_val) + start

            max_vals.append(ValPair(next_val, next_index))

        return int("".join([val.value_str for val in max_vals]))


def parse(inpt: str) -> list[Bank]:
    return [Bank([int(val) for val in list(line)]) for line in inpt.split()]


def find_total_joltage(inpt: str, length: int) -> int:
    banks = parse(inpt)

    max_joltages = []
    for b in banks:
        max_joltages.append(b.find_max_joltage(length=length))

    return sum(max_joltages)


with open("03_input") as f:
    data = f.read()

assert find_total_joltage(example, length=2) == 357
assert find_total_joltage(data, length=2) == 17330

assert find_total_joltage(example, length=12) == 3121910778619
assert find_total_joltage(data, length=12) == 171518260283767
