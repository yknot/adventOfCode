import functools

example = """125 17"""


def parse_data(data):
    stones = [int(e) for e in data.split()]
    return stones


@functools.cache
def blink(stone):
    if stone == 0:
        return (1, None)
    elif len(str(stone)) % 2 == 0:
        half = len(str(stone)) // 2
        string = str(stone)
        return (int(string[:half]), int(string[half:]))
    else:
        return (stone * 2024, None)


@functools.cache
def blink_depth(stone, n_blinks):
    left, right = blink(stone)

    if n_blinks == 1:
        return 2 if right is not None else 1

    count = blink_depth(left, n_blinks - 1)
    if right is not None:
        count += blink_depth(right, n_blinks - 1)

    return count


def calculate_blinks(data, n_blinks):
    stones = parse_data(data)

    total = 0
    for s in stones:
        total += blink_depth(s, n_blinks)

    return total


res = calculate_blinks(example, 6)
assert res == 22, res

res = calculate_blinks(example, 25)
assert res == 55312, res

with open("11_input") as f:
    res = calculate_blinks(f.read(), 25)
    assert res == 189092, res

with open("11_input") as f:
    res = calculate_blinks(f.read(), 75)
    assert res == 224869647102559, res
