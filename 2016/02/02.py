import numpy as np


directions = open('input').read().splitlines()

keypad = np.array([['-', '-', '1', '-', '-'],
                   ['-', '2', '3', '4', '-'],
                   ['5', '6', '7', '8', '9'],
                   ['-', 'A', 'B', 'C', '-'],
                   ['-', '-', 'D', '-', '-']])
passcode = ''
spot = [2, 0]
for code in directions:
    for d in code:
        if d == 'U' and spot[0] > 0:
            if keypad[tuple([spot[0] - 1, spot[1]])] != '-':
                spot[0] -= 1
        elif d == 'D' and spot[0] < keypad.shape[0] - 1:
            if keypad[tuple([spot[0] + 1, spot[1]])] != '-':
                spot[0] += 1
        elif d == 'R' and spot[1] < keypad.shape[1] - 1:
            if keypad[tuple([spot[0], spot[1] + 1])] != '-':
                spot[1] += 1
        elif d == 'L' and spot[1] > 0:
            if keypad[tuple([spot[0], spot[1] - 1])] != '-':
                spot[1] -= 1

    passcode += keypad[tuple(spot)]


print(passcode)
