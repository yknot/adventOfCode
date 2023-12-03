"""
Day 2, part 2
"""
from utils import read_input


test_inpt = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


def check_game(games):
    total_power = 0
    for _, draws in games:
        counts = {"red": 0, "blue": 0, "green": 0}
        for d in draws:
            for k, v in counts.items():
                if d.get(k, 0) > v:
                    counts[k] = d[k]

        total_power += counts["red"] * counts["blue"] * counts["green"]

    return total_power


def parse(line):
    game, draws = line.split(":")
    _, gid = game.split(" ")
    gid = int(gid)

    draws = draws.split(";")
    draws_list = []
    for draw in draws:
        draw_dict = {}
        for d in draw.split(","):
            num, color = d.strip().split(" ")
            draw_dict[color] = int(num)
        draws_list.append(draw_dict)

    return gid, draws_list


inpt = list(read_input(2, line_parser=parse))

test = [parse(t) for t in test_inpt]

assert check_game(test) == 2286

assert check_game(inpt) == 63981
