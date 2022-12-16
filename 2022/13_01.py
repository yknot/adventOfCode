"""
Day 13
"""


def check_pair(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return "correct"
        elif left > right:
            return "incorrect"
        else:
            return "equal"
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            ret = check_pair(l, r)
            if ret in ["correct", "incorrect"]:
                return ret

        if len(left) < len(right):
            return "correct"
        elif len(left) > len(right):
            return "incorrect"
        else:
            return "equal"
    elif isinstance(left, list) and isinstance(right, int):
        return check_pair(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return check_pair([left], right)


def check_order(inpt):
    i = 0
    idx = 1
    total = 0
    while i < len(inpt):
        left = inpt[i]
        right = inpt[i + 1]

        correct_order = check_pair(left, right)

        if correct_order == "correct":
            total += idx

        i += 3
        idx += 1

    return total


test_inpt = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def parser(line):
    if line:
        return eval(line)
    return None


test_parsed = [parser(line) for line in test_inpt.split("\n")]
assert check_order(test_parsed) == 13

parsed = []
with open("13_input") as f:
    for line in f:
        parsed.append(parser(line.strip("\n")))
assert check_order(parsed) == 5557
