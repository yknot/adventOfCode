
def test_passphrase(string):
    """test validity of passphrase"""
    words = set()
    for w in string.split():
        w_tmp = ''.join(sorted(w))
        if w_tmp in words:
            return False
        words.add(w_tmp)

    return True


assert test_passphrase("abcde fghij")
assert not test_passphrase("abcde xyz ecdab")
assert test_passphrase("a ab abc abd abf abj")
assert test_passphrase("iiii oiii ooii oooi oooo")
assert not test_passphrase("oiii ioii iioi iiio")

raw = open('input').read().split('\n')
total = 0
for r in raw:
    if test_passphrase(r):
        total += 1

print(total)
