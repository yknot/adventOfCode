"""
Day 5
"""


def get_message(inpt):
    containers, instructions = parse(inpt)

    for n, x, y in instructions:
        x, y = x - 1, y - 1
        to_add = containers[x][-n:][::-1]
        containers[y] += to_add
        containers[x] = containers[x][:-n]

    final = ""
    for c in containers:
        final += c[-1]

    return final


def parse(inpt):
    i = 0
    while i < len(inpt):
        if not inpt[i]:
            break
        i += 1

    n_containers = int(inpt[i - 1].split()[-1])
    containers = [list() for _ in range(n_containers)]

    for line in inpt[i - 2 :: -1]:
        j = 0
        k = 0
        while j < len(line):
            if line[j + 1 : j + 2] != " ":
                containers[k].append(line[j + 1 : j + 2])

            j += 4
            k += 1

    instructions = []
    for inst in inpt[i + 1 :]:
        line = inst.split()
        instructions.append((int(line[1]), int(line[3]), int(line[5])))

    return containers, instructions


with open("05_test_input") as f:
    test_inpt = f.read().split("\n")

with open("05_input") as f:
    inpt = f.read().split("\n")

assert get_message(test_inpt) == "CMZ"

assert get_message(inpt) == "WHTLRMZRC"
