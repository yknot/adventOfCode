class Navigate(object):
    def __init__(self, maze):
        """navigate the maze"""
        # get start
        self.row = 0
        self.col = maze[0].index('|')
        # store letters found
        self.letters = []
        self.direction = 'down'

        self.maze = maze

    def one_step(self):
        """move in self.direction"""
        if self.direction == 'down':
            self.row += 1
        elif self.direction == 'up':
            self.row -= 1
        elif self.direction == 'right':
            self.col += 1
        elif self.direction == 'left':
            self.col -= 1

    def search(self):
        """search around for next direction"""
        if self.direction in ['up', 'down']:
            if self.maze[self.row][self.col - 1] != ' ':
                self.direction = 'left'
            elif self.maze[self.row][self.col + 1] != ' ':
                self.direction = 'right'
        else:
            if self.maze[self.row - 1][self.col] != ' ':
                self.direction = 'up'
            elif self.maze[self.row + 1][self.col] != ' ':
                self.direction = 'down'

    def move(self):
        """move one step"""
        self.one_step()

        if self.maze[self.row][self.col] == ' ':
            return True
        elif self.maze[self.row][self.col] == '+':
            self.search()
        elif self.maze[self.row][self.col].isalpha():
            self.letters.append(self.maze[self.row][self.col])

    def run(self):
        """run through the maze"""
        while True:
            res = self.move()
            # found the end
            if res is not None:
                break

        return ''.join(self.letters)



test = Navigate(open('testinput').read().splitlines())
assert test.run() == 'ABCDEF'

valid = Navigate(open('input').read().splitlines())
print(valid.run())
