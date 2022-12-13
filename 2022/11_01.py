"""
Day 11
"""
from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    items: list[int]
    operation: Callable
    test: Callable

    def string(self):
        return f"  Items: {self.items}\n"


@dataclass
class Container:
    monkies: list[Monkey]

    def __repr__(self):
        return self.string()

    def string(self):
        res = ""
        for i, m in enumerate(self.monkies):
            res += f"Monkey {i}:\n"
            res += m.string()
            res += "\n"
        return res


def run_monkies(container: Container):

    inspected = {i: 0 for i in range(len(container.monkies))}

    for i in range(20):

        for j, m in enumerate(container.monkies):
            while m.items:
                inspected[j] += 1
                item = m.items.pop(0)
                item = m.operation(item)
                item = item // 3
                move = m.test(item)
                container.monkies[move].items.append(item)

    a, b = sorted(inspected.values(), reverse=True)[:2]
    return a * b


test_c = Container(
    monkies=[
        Monkey(
            items=[79, 98],
            operation=lambda x: x * 19,
            test=lambda x: 2 if x % 23 == 0 else 3,
        ),
        Monkey(
            items=[54, 65, 75, 74],
            operation=lambda x: x + 6,
            test=lambda x: 2 if x % 19 == 0 else 0,
        ),
        Monkey(
            items=[79, 60, 97],
            operation=lambda x: x**2,
            test=lambda x: 1 if x % 13 == 0 else 3,
        ),
        Monkey(
            items=[74],
            operation=lambda x: x + 3,
            test=lambda x: 0 if x % 17 == 0 else 1,
        ),
    ]
)

inpt = Container(
    monkies=[
        Monkey(
            items=[61],
            operation=lambda x: x * 11,
            test=lambda x: 7 if x % 5 == 0 else 4,
        ),
        Monkey(
            items=[76, 92, 53, 93, 79, 86, 81],
            operation=lambda x: x + 4,
            test=lambda x: 2 if x % 2 == 0 else 6,
        ),
        Monkey(
            items=[91, 99],
            operation=lambda x: x * 19,
            test=lambda x: 5 if x % 13 == 0 else 0,
        ),
        Monkey(
            items=[58, 67, 66],
            operation=lambda x: x**2,
            test=lambda x: 6 if x % 7 == 0 else 1,
        ),
        Monkey(
            items=[94, 54, 62, 73],
            operation=lambda x: x + 1,
            test=lambda x: 3 if x % 19 == 0 else 7,
        ),
        Monkey(
            items=[59, 95, 51, 58, 58],
            operation=lambda x: x + 3,
            test=lambda x: 0 if x % 11 == 0 else 4,
        ),
        Monkey(
            items=[87, 69, 92, 56, 91, 93, 88, 73],
            operation=lambda x: x + 8,
            test=lambda x: 5 if x % 3 == 0 else 2,
        ),
        Monkey(
            items=[71, 57, 86, 67, 96, 95],
            operation=lambda x: x + 7,
            test=lambda x: 3 if x % 17 == 0 else 1,
        ),
    ]
)


assert run_monkies(test_c) == 10605

assert run_monkies(inpt) == 76728
