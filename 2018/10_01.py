"""
Day 10 part 1
"""
from utils import read_input, integers


class Point:
    def __init__(self, x: int, y: int, del_x: int, del_y: int) -> None:
        self.x = x
        self.y = y
        self.del_x = del_x
        self.del_y = del_y

    def move(self) -> None:
        self.x += self.del_x
        self.y += self.del_y

    def unmove(self) -> None:
        self.x -= self.del_x
        self.y -= self.del_y


def print_board(pts, range_x, min_x, range_y, min_y):
    board = [["."] * range_x for _ in range(range_y)]

    for p in pts:
        board[p.y - min_y - 1][p.x - min_x - 1] = "#"

    for line in board:
        print("".join(line))


def find_word(pts):
    points = []
    for p in pts:
        points.append(Point(*p))

    prev_x, prev_y = 1000000, 1000000

    idx = 0

    while True:
        max_x, max_y = 0, 0
        min_x, min_y = 1000000, 1000000
        for p in points:
            p.move()
            if p.x > max_x:
                max_x = p.x
            if p.x < min_x:
                min_x = p.x
            if p.y > max_y:
                max_y = p.y
            if p.y < min_y:
                min_y = p.y

        if prev_x < (max_x - min_x) or prev_y < (max_y - min_y):
            for p in points:
                p.unmove()
            print_board(points, max_x - min_x, min_x, max_y - min_y, min_y)
            return idx

        prev_x = max_x - min_x
        prev_y = max_y - min_y
        idx += 1


test_inpt = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""

test_inpt = tuple(integers(x) for x in test_inpt.split("\n"))
assert find_word(test_inpt) == 3

inpt = read_input(10, line_parser=integers)
assert find_word(inpt) == 10630
