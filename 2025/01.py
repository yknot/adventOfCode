from dataclasses import dataclass, field

example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


@dataclass
class Step:
    direction: str
    number: int


@dataclass
class Dial:
    dial: int = 50
    count: int = 0
    dir_map: dict = field(default_factory=lambda: {"R": 1, "L": -1})

    def run_step(self, step: Step, any_click: bool = False):

        started_at_zero = self.dial % 100 == 0
        before = self.dial // 100

        # move the dial
        self.dial += self.dir_map[step.direction] * step.number

        if any_click:
            self.count += abs((self.dial // 100) - before)
            # if we already started at 0 and moved left don't double count crossing
            if started_at_zero and step.direction == "L":
                self.count -= 1
        if self.dial % 100 == 0:
            # we cross the 0 line don't double count
            if any_click and step.direction == "R":
                pass
            else:
                self.count += 1


def parse(inpt: str):
    steps = []
    for line in inpt.split():
        steps.append(Step(direction=line[0], number=int(line[1:])))

    return steps


def compute_password(inpt: str, any_click: bool = False):

    dial = Dial()
    steps = parse(inpt)

    for step in steps:
        dial.run_step(step, any_click=any_click)

    return dial.count


assert compute_password(example) == 3

with open("01_input") as f:
    assert compute_password(f.read()) == 1026


assert compute_password(example, any_click=True) == 6

with open("01_input") as f:
    assert compute_password(f.read(), any_click=True) == 5923
