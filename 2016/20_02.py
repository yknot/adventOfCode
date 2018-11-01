def preprocess(l):
    """convert lines to tuples"""
    r = []
    # split and cast to ints
    for line in l:
        bot, top = line.split('-')
        r.append([int(bot), int(top)])
    return sorted(r)


def find_all(blacklist, tot):
    """find the min value allowed"""
    # reduce to non-overlapping windows
    shrunken = []
    for r in blacklist:
        add = True
        for s in shrunken:
            # if windows are overlapping
            if s[0] <= r[0] <= s[1] or s[0] <= r[1] <= s[1]:
                s[0] = min(s[0], r[0])
                s[1] = max(s[1], r[1])
                add = False
                break

        if add:
            shrunken.append(list(r))

    # calculate total
    for s in shrunken:
        tot -= (s[1] - s[0] + 1)

    return tot


lines = ['5-8', '0-2', '4-7']

assert find_all(preprocess(lines), 10) == 2

lines = open('20_input').read().split('\n')
print(find_all(preprocess(lines), 4294967296))
