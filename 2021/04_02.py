"""
Day 4
"""
from utils import read_input


class Board:
    def __init__(self, lines):
        self.board = []
        for line in lines:
            self.board.append([int(l) for l in line.split()])
        self.marked = [[0] * len(self.board[0]) for _ in range(len(self.board))]

    def __repr__(self):
        output = ""
        for b_line, m_line in zip(self.board, self.marked):
            output += " ".join([f"{l:02}" for l in b_line])
            output += "\t"
            output += " ".join([str(l) for l in m_line])
            output += "\n"
        return output

    def mark(self, val):
        for i, line in enumerate(self.board):
            for j, l in enumerate(line):
                if l == val:
                    self.marked[i][j] = 1

    def check(self):
        # check rows
        for line in self.marked:
            if all(line):
                return True

        # check cols
        for i in range(len(self.marked[0])):
            flag = True
            for m_line in self.marked:
                if not m_line[i]:
                    flag = False
                    break
            if flag:
                return True

        return False

    def sum(self):
        total = 0
        for b_line, m_line in zip(self.board, self.marked):
            for b, m in zip(b_line, m_line):
                if not m:
                    total += b

        return total


def bingo(inpt):
    order = [int(i) for i in inpt[0].split(",")]

    boards = []
    lines = []
    for line in inpt[2:]:
        if line != "":
            lines.append(line)
        else:
            boards.append(Board(lines))
            lines = []
    boards.append(Board(lines))

    won = [0] * len(boards)
    for o in order:
        for i, b in enumerate(boards):
            if won[i]:
                continue
            b.mark(o)
            if b.check():
                won[i] = 1
                if all(won):
                    return b.sum() * o


test_inpt = [l.strip() for l in open("04_test_input").readlines()]
assert bingo(test_inpt) == 1924

inpt = list(read_input(4))
assert bingo(inpt) == 13912
