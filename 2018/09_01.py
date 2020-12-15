"""
Day 9 part 1

Rules
- Place marble between the 
"""


def find_winner(n_players, n_marbles):
    marbles = [0]

    i = 1
    idx = 0
    player = 0
    player_scores = [0] * n_players
    while i != n_marbles + 1:
        idx += 1
        if idx >= len(marbles):
            idx = idx - len(marbles)

        if i % 23 == 0:
            player_scores[player] += i
            idx -= 8

            if idx < 0:
                idx = len(marbles) + idx

            removed = marbles.pop(idx)
            player_scores[player] += removed

        else:
            marbles.insert(idx + 1, i)
            idx += 1

        i += 1
        player += 1
        if player == n_players:
            player = 0

    return max(player_scores)


assert find_winner(9, 25) == 32
assert find_winner(10, 1618) == 8317
assert find_winner(13, 7999) == 146373
assert find_winner(17, 1104) == 2764
assert find_winner(21, 6111) == 54718
assert find_winner(30, 5807) == 37305

assert find_winner(423, 71944) == 418237
