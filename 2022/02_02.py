"""
Day 2
"""
from utils import read_input


test_inpt = """A Y
B X
C Z"""

scores = {"X": 1, "Y": 2, "Z": 3}
loss = {"A": "Z", "B": "X", "C": "Y"}
win = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B": "Y", "C": "Z"}


def compute_score(vals):
    score = 0
    for pair in vals:
        x, y = pair.split()
        if y == "X":
            score += scores[loss[x]]
        elif y == "Y":
            score += scores[draw[x]]
            score += 3
        elif y == "Z":
            score += scores[win[x]]
            score += 6

    return score


inpt = list(read_input(2))

assert compute_score(test_inpt.split("\n")) == 12

assert compute_score(inpt) == 14470
