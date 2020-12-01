"""
Day 9 part 2

Rules
- Place marble between the 
"""

from collections import deque


def find_winner(n_players: int, n_marbles: int) -> int:
    marbles = deque([0])

    multiple = 23
    i = 1
    player = 0
    player_scores = [0] * n_players

    while i < n_marbles + 1:
        marbles.rotate(-2)

        if i == multiple:
            multiple += 23
            marbles.rotate(9)

            removed = marbles.popleft()
            player_scores[player] += removed
            player_scores[player] += i

        else:
            marbles.appendleft(i)

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

assert find_winner(423, 7194400) == 3505711612

