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

    def solve(self):
        """find number of open spaces"""
        open_spaces = 0
        for _ in range(self.n):
            open_spaces += self.line.count(".")

            new_line = ""
            self.line = "." + self.line + "."
            for j, l in enumerate(self.line[1:-1]):
                if trap(self.line[j], l, self.line[j + 2]):
                    new_line += "^"
                else:
                    new_line += "."
            self.line = new_line

        return open_spaces


assert Maze("..^^.", 3).solve() == 6
assert Maze(".^^.^.^^^^", 10).solve() == 38

input_line = (
    ".^.^..^......^^^^^...^^^...^...^....^^.^...^."
    + "^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^"
)

print(Maze(input_line, 40).solve())
