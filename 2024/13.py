example = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


class Machine:
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize

    def solve(self):
        """solve as a system of equations"""
        solve_b = (self.prize[0] * self.a[1] - self.prize[1] * self.a[0]) / (
            self.a[1] * self.b[0] - self.a[0] * self.b[1]
        )
        solve_a = (self.prize[0] - self.b[0] * solve_b) / self.a[0]
        # if integer then there is a solution otherwise it would require partial steps
        if solve_a.is_integer() and solve_b.is_integer():
            return int(solve_a), int(solve_b)
        return 0, 0


def parse_data(data, conversion=False):
    machines = []
    for row in data.split("\n\n"):
        raw_a, raw_b, raw_prize = row.split("\n")

        a_x = int(raw_a.split()[2][1:-1])
        a_y = int(raw_a.split()[3][1:])

        b_x = int(raw_b.split()[2][1:-1])
        b_y = int(raw_b.split()[3][1:])

        prize_x = int(raw_prize.split()[1][2:-1])
        prize_y = int(raw_prize.split()[2][2:])

        if conversion:
            prize_x += 10000000000000
            prize_y += 10000000000000

        machines.append(Machine((a_x, a_y), (b_x, b_y), (prize_x, prize_y)))

    return machines


def calculate_prizes(data, conversion=False):
    machines = parse_data(data, conversion)

    total = 0
    possible = []
    for i, machine in enumerate(machines):
        a, b = machine.solve()
        if a != 0 and b != 0:
            possible.append(i)
        total += (3 * a) + b

    return total, possible


res, possible = calculate_prizes(example)
assert possible == [0, 2], possible
assert res == 480, res

with open("13_input") as f:
    res, _ = calculate_prizes(f.read())
    assert res == 38839, res

_, possible = calculate_prizes(example, conversion=True)
assert possible == [1, 3], possible

with open("13_input") as f:
    res, _ = calculate_prizes(f.read(), conversion=True)
    assert res == 75200131617108, res
