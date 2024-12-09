example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def parse_data(data):
    lines = []
    for line in data.split("\n"):
        lines.append([int(a) for a in line.split()])

    return lines


def check_row(line):
    ascending = True if line[0] < line[1] else False
    safe = True
    for a, b in zip(line, line[1:]):
        if ascending and a > b:
            safe = False
            break
        elif not ascending and a < b:
            safe = False
            break
        elif abs(a - b) == 0 or abs(a - b) > 3:
            safe = False
            break

    return safe


def find_safe_rows(data):
    lines = parse_data(data)

    safe_count = 0
    for line in lines:
        if check_row(line):
            safe_count += 1

    return safe_count


def find_safe_rows_mod(data):
    lines = parse_data(data)
    safe_count = 0
    for line in lines:
        if check_row(line):
            safe_count += 1
            continue

        for i, _ in enumerate(line):
            line_copy = line.copy()
            line_copy.pop(i)
            if check_row(line_copy):
                safe_count += 1
                break

    return safe_count


assert find_safe_rows(example) == 2

with open("02_input") as f:
    assert find_safe_rows(f.read()) == 230


assert find_safe_rows_mod(example) == 4

with open("02_input") as f:
    assert find_safe_rows_mod(f.read()) == 301
