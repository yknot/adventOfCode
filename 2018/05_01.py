"""
Day 5 Part 1
"""
from utils import read_input


def combine(seq):
    if not isinstance(seq, list):
        seq = list(seq)
    mod = True
    while mod:
        idx = 0
        mod = False
        while idx + 1 < len(seq):
            if seq[idx].lower() == seq[idx + 1].lower() and seq[idx] != seq[idx + 1]:
                del seq[idx]
                del seq[idx]
                mod = True
            else:
                idx += 1

    return "".join(seq)


result = combine("dabAcCaCBAcCcaDA")
assert result == "dabCBAcaDA"
assert len(result) == 10

assert len(combine(read_input(5))) == 10584
