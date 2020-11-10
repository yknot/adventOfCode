"""
Day 5 Part 2
"""
from utils import read_input


def run_all(seq):
    options = set(s.lower() for s in set(seq))

    min_result = None
    min_result_len = len(seq)

    for o in options:
        new_seq = [s for s in seq if s not in [o, o.upper()]]
        result = combine(new_seq)
        if len(result) < min_result_len:
            min_result_len = len(result)
            min_result = result

    return min_result


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


result = run_all("dabAcCaCBAcCcaDA")
assert result == "daDA"
assert len(result) == 4

assert len(run_all(read_input(5))) == 6968
