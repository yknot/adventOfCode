def parse_garbage(data):
    """parse a string of garbage"""
    level = 0
    score = 0
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
            continue
        elif c == '<':          # catch start of garbage
            in_garbage = True
        elif c == '{':          # catch open group
            level += 1
        elif c == '}':          # catch close group
            score += level
            level -= 1

    return score


tests = {
    '{}': 1,
    '{{{}}}': 6,
    '{{},{}}': 5,
    '{{{},{},{{}}}}': 16,
    '{<a>,<a>,<a>,<a>}': 1,
    '{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
    '{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
    '{{<a!>},{<a!>},{<a!>},{<ab>}}': 3
}

# "unit" tests
for k, v in tests.items():
    assert parse_garbage(k) == v


print(parse_garbage(open('input').read().strip()))
