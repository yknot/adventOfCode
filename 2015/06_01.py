""" Day 6 advent of code """
import numpy as np



def main():
    """calculate light intensity"""

    instructions = open('input').readlines()


    lights = np.zeros((1000, 1000))


    for i in instructions:
        cmd = i.split()
        if cmd[0] == 'turn':
            action = cmd[1]
            start = cmd[2].split(',')
            start = [int(s) for s in start]
            end = cmd[4].split(',')
            end = [int(e) for e in end]
            if action == 'off':
                lights[start[0]:end[0]+1, start[1]:end[1]+1] -= 1
                lights[lights < 0] = 0

            else:
                lights[start[0]:end[0]+1, start[1]:end[1]+1] += 1

        else:
            start = cmd[1].split(',')
            start = [int(s) for s in start]
            end = cmd[3].split(',')
            end = [int(e) for e in end]
            lights[start[0]:end[0]+1, start[1]:end[1]+1] += 2

    lights[lights < 0] = 0

    print int(sum(sum(lights)))

if __name__ == "__main__":
    main()





