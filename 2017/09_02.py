def parse_garbage(data):
    """parse a string of garbage"""
    garbage_count = 0
    skip = False
    in_garbage = False
    for c in data:
        if skip:                # if skip from previous iter
            skip = False
            continue
        elif c == '!':          # if bang then skip next character
            skip = True
        elif c == '>':          # leave garbage
            in_garbage = False
        elif in_garbage:        # if in garbage then continue
            garbage_count += 1
        elif c == '<':          # catch start of garbage
            in_garbage = True

    return garbage_count


tests = {
    '<>': 0,
    '<random characters>': 17,
    '<<<<>': 3,
    '<{!>}>': 2,
    '<!!>': 0,
    '<!!!>>': 0,
    '<{o"i!a,<{i<a>': 10
}

# "unit" tests
for k, v in tests.items():
    assert parse_garbage(k) == v


print(parse_garbage(open('input').read().strip()))
