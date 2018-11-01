def preprocess(l):
    """convert lines to tuples"""
    r = []
    # split and cast to ints
    for line in l:
        bot, top = line.split('-')
        r.append((int(bot), int(top)))
    return sorted(r)


def find_min(blacklist):
    """find the min value allowed"""
    bot = 0
    for r in blacklist:
        if r[0] <= bot <= r[1]:
            bot = r[1] + 1

    return bot


lines = ['5-8', '0-2', '4-7']

assert find_min(preprocess(lines)) == 3

lines = open('20_input').read().split('\n')
print(find_min(preprocess(lines)))
