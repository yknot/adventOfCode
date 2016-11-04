import re


grid = [o.strip() for o in open('input').readlines()]


for _ in range(100):
    lights = 0
    newGrid = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j == 0:
                newGrid.append('')
            count = 0
            
            # top left
            if i - 1 >= 0 and j - 1 >= 0:
                if grid[i-1][j-1] == '#':
                    count += 1
            # top
            if i - 1 >= 0: 
                if grid[i-1][j] == '#':
                    count += 1
            # top right
            if i - 1 >= 0 and j + 1 < len(grid):
                if grid[i-1][j+1] == '#':
                    count += 1
            # right
            if j + 1 < len(grid):
                if grid[i][j+1] == '#':
                    count += 1
            # left
            if j - 1 >= 0:
                if grid[i][j-1] == '#':
                    count += 1
            # bottom left
            if i + 1 < len(grid) and j - 1 >= 0:
                if grid[i+1][j-1] == '#':
                    count += 1
            # bottom
            if i + 1 < len(grid):
                if grid[i+1][j] == '#':
                    count += 1
            # bottom right
            if i + 1 < len(grid) and j + 1 < len(grid):
                if grid[i+1][j+1] == '#':
                    count += 1                

            if grid[i][j] == '#' and (count == 2 or count == 3):
                newGrid[i] += '#'
            elif grid[i][j] == '.' and count == 3:
                newGrid[i] += '#'             
            elif grid[i][j] == '#':
                newGrid[i] += '.'
            else:
                newGrid[i] += '.'                


    grid = newGrid

    grid[0] = '#' + grid[0][1:-1] + '#'
    grid[-1] = '#' + grid[-1][1:-1] + '#'

    for line in grid:
        lights += len([m.start() for m in re.finditer('#', line)])


print lights
