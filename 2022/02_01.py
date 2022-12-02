"""
Day 2
"""
from utils import read_input


test_inpt = """A Y
B X
C Z"""

scores = {"X": 1, "Y": 2, "Z": 3}
loss = [("A", "Z"), ("B", "X"), ("C", "Y")]
win = [("A", "Y"), ("B", "Z"), ("C", "X")]
draw = [("A", "X"), ("B", "Y"), ("C", "Z")]


def compute_score(vals):
    score = 0
    for pair in vals:
        x, y = pair.split()
        if (x, y) in draw:
            score += 3
        elif (x, y) in win:
            score += 6
        score += scores[y]

    return score


inpt = list(read_input(2))

assert compute_score(test_inpt.split("\n")) == 15

assert compute_score(inpt) == 12679
