example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def parse_data(data):
    equations = []
    for line in data.split("\n"):
        target, rest = line.split(":")
        rest = [int(r) for r in rest.split()]
        equations.append((int(target), rest))

    return equations


def solve(target, values, current, with_concat=False):
    # since operations only increase current value
    if current > target:
        return False

    # reached end of values
    if not values:
        if current == target:
            return True
        return False

    # starting point
    if current == -1:
        results = []
        if with_concat:
            results.append(
                solve(
                    target,
                    values[2:],
                    int(str(values[0]) + str(values[1])),
                    with_concat=with_concat,
                )
            )
        results.append(
            solve(target, values[2:], values[0] + values[1], with_concat=with_concat)
        )
        results.append(
            solve(target, values[2:], values[0] * values[1], with_concat=with_concat)
        )
        return any(results)

    results = []
    if with_concat:
        results.append(
            solve(
                target,
                values[1:],
                int(str(current) + str(values[0])),
                with_concat=with_concat,
            )
        )
    results.append(
        solve(target, values[1:], current + values[0], with_concat=with_concat)
    )
    results.append(
        solve(target, values[1:], current * values[0], with_concat=with_concat)
    )
    return any(results)


def solve_equations(data, with_concat=False):
    equations = parse_data(data)

    total = 0
    for target, values in equations:
        if solve(target, values, -1, with_concat=with_concat):
            total += target

    return total


res = solve_equations(example)
assert res == 3749, res

with open("07_input") as f:
    res = solve_equations(f.read())
    assert res == 3312271365652, res

res = solve_equations(example, with_concat=True)
assert res == 11387, res

with open("07_input") as f:
    res = solve_equations(f.read(), with_concat=True)
    assert res == 509463489296712, res
