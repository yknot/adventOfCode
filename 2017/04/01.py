
def test_passphrase(string):
    """test validity of passphrase"""
    words = set()
    for w in string.split():
        if w in words:
            return False
        words.add(w)

    return True


assert test_passphrase("aa bb cc dd ee") == True
assert test_passphrase("aa bb cc dd aa") == False
assert test_passphrase("aa bb cc dd aaa") == True

raw = open('input').read().split('\n')
total = 0
for r in raw:
    if test_passphrase(r):
        total += 1

print(total)
