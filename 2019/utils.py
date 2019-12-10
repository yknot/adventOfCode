"""utility functions to be used in solving the puzzles"""
import re


def read_input(day, line_parser=str.strip, file_template="{:02}_input"):
    "read the input file and pass it back"
    return mapt(line_parser, open(file_template.format(day)))


def integers(text):
    "cast the read in vals to integers where possible"
    return mapt(int, re.findall(r"-?\d+", text))


def mapt(fn, *args):
    "tupe the results of the map"
    return tuple(map(fn, *args))


cat = "".join


def read_integers(*args):
    "run read input but return tuple of integers"
    return list(integers(cat(read_input(*args))))


def ints(l):
    "take a list and cast to ints"
    return [int(i) for i in l]
