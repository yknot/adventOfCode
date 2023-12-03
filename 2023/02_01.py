"""
Day 2
"""
from utils import read_input


test_inpt = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

max_red = 12
max_green = 13
max_blue = 14


def check_game(games):
    total_ids = 0
    for gid, draws in games:
        for d in draws:
            if d.get("red", 0) > max_red:
                break
            if d.get("green", 0) > max_green:
                break
            if d.get("blue", 0) > max_blue:
                break
        else:
            total_ids += gid

    return total_ids


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

assert check_game(test) == 8

assert check_game(inpt) == 2449
