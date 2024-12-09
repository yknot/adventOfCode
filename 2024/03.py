import re

example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
new_example = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)


def sum_mults(data):
    regex = r"mul\((\d+),(\d+)\)"
    matches = re.finditer(regex, data, re.MULTILINE)

    total = 0
    for match in matches:
        a, b = match.groups()
        total += int(a) * int(b)

    return total


def sum_mults_do_dont(data):
    dont_locs = [m.start() for m in re.finditer(r"don't\(\)", data, re.MULTILINE)]
    do_locs = [m.start() for m in re.finditer(r"do\(\)", data, re.MULTILINE)]

    loc = 0
    i, j = 0, 0
    enabled_sectors = []
    enabled = True
    while i < len(dont_locs) or j < len(do_locs):
        if j == len(do_locs) or (i != len(dont_locs) and dont_locs[i] < do_locs[j]):
            if enabled:
                enabled_sectors.append([loc, dont_locs[i]])
                enabled = False
            i += 1

        else:
            if not enabled:
                loc = do_locs[j]
                enabled = True
            j += 1

    if enabled:
        enabled_sectors.append([loc, len(data)])

    regex = r"mul\((\d+),(\d+)\)"
    matches = re.finditer(regex, data, re.MULTILINE)

    total = 0
    for match in matches:
        start = match.start()
        safe = False
        for i, j in enabled_sectors:
            if start > i and start < j:
                safe = True
                break

        if safe:
            a, b = match.groups()
            total += int(a) * int(b)

    return total


res = sum_mults(example)
assert res == 161, res

with open("03_input") as f:
    res = sum_mults(f.read())
    assert res == 183788984, res

res = sum_mults_do_dont(new_example)
assert res == 48, res

with open("03_input") as f:
    res = sum_mults_do_dont(f.read())
    assert res == 62098619, res
