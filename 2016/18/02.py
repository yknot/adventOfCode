"""day 18 advent of code 2016"""


def trap(l, c, r):
    """calculate if there is a trap at the specified spot"""
    if l == "^" and c == "^" and r == ".":
        return True
    elif l == "." and c == "^" and r == "^":
        return True
    elif l == "^" and c == "." and r == ".":
        return True
    elif l == "." and c == "." and r == "^":
        return True
    return False


class Maze(object):
    """object to take in the first line and run solve"""

    def __init__(self, line, n):
        self.line = line
        self.n = n
        self.past = {}

    def solve_ten(self, ten):
        """find next 10 piece (technically 12)"""
        if ten in self.past:
            return self.past[ten]

        new_ten = ""
        for j, l in enumerate(ten[1:-1]):
            if trap(ten[j], l, ten[j + 2]):
                new_ten += "^"
            else:
                new_ten += "."
        self.past[ten] = new_ten
        return new_ten

    def solve(self):
        """find number of open spaces"""
        open_spaces = 0
        for _ in range(self.n):
            open_spaces += self.line.count(".")
            new_line = ""
            for k in range(0, 100, 10):
                if k == 0:
                    ten = "." + self.line[k : k + 10] + self.line[k + 10]
                elif k == (100 - 10):
                    ten = self.line[k - 1] + self.line[k : k + 10] + "."
                else:
                    ten = self.line[k - 1] + self.line[k : k + 10] + self.line[k + 10]

                new_line += self.solve_ten(ten)

            self.line = new_line

        return open_spaces


# assert Maze("..^^.", 3).solve() == 6
# assert Maze(".^^.^.^^^^", 10).solve() == 38

input_line = (
    ".^.^..^......^^^^^...^^^...^...^....^^.^...^."
    + "^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^"
)
m = Maze(input_line, 400000)
sol = m.solve()
assert sol == 19984714
