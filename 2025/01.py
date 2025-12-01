from dataclasses import dataclass

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


DIR_MAP = {"R": 1, "L": -1}


@dataclass
class Step:
    direction: str
    number: int


@dataclass
class Dial:
    dial: int = 50
    count: int = 0

    @property
    def rotations(self):
        return self.dial // 100

    @property
    def position(self):
        return self.dial % 100

    def run_step(self, step: Step, any_click: bool = False):

        old_rotations = self.rotations
        started_at_zero = self.position == 0

        # move the dial
        self.dial += DIR_MAP[step.direction] * step.number

        crossings = abs(self.rotations - old_rotations)

        if any_click:
            self.count += crossings
            # if we started exactly at 0 and moved left, we overcounted by 1
            if started_at_zero and step.direction == "L":
                self.count -= 1

        if self.position == 0:
            # if any_click and we already counted crossings from a rightward move
            if not (any_click and step.direction == "R"):
                self.count += 1


def parse(inpt: str) -> list[Step]:
    return [Step(line[0], int(line[1:])) for line in inpt.split()]


def compute_password(inpt: str, any_click: bool = False) -> int:

    dial = Dial()
    steps = parse(inpt)

    for step in steps:
        dial.run_step(step, any_click=any_click)

    return dial.count


with open("01_input") as f:
    data = f.read()

assert compute_password(example) == 3, compute_password(example)
assert compute_password(data) == 1026, compute_password(data)
assert compute_password(example, any_click=True) == 6, compute_password(
    example, any_click=True
)
assert compute_password(data, any_click=True) == 5923, compute_password(
    data, any_click=True
)
