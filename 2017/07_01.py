def find_root(filename):
    raw = open(filename).read()
    progs = [l.split(' ')[0] for l in raw.split('\n') if not l.endswith(')')]

    res = [p for p in progs if raw.count(p) == 1]
    assert len(res) == 1
    return res[0]


assert find_root('test_input') == 'tknk'

print(find_root('input'))
