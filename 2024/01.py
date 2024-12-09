example = """3   4
4   3
2   5
1   3
3   9
3   3"""


def parse_data(data):
    left, right = [], []
    for line in data.split("\n"):
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    return left, right


def find_diffs(data):
    left, right = parse_data(data)

    left = sorted(left)
    right = sorted(right)

    total = 0
    for l, r in zip(left, right):
        total += abs(r - l)

    return total


def find_similarity(data):
    left, right = parse_data(data)

    total = 0
    for l in left:
        total += l * right.count(l)

    return total


assert find_diffs(example) == 11
with open("01_input") as f:
    assert find_diffs(f.read()) == 2742123

assert find_similarity(example) == 31
with open("01_input") as f:
    assert find_similarity(f.read()) == 21328497
