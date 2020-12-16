"""

Day 7 part 2

"""
from utils import read_input


def parser(line):
    parts = line.split("bag")
    bag = parts[0].strip()
    bags = []
    for p in parts[1:]:
        if "no other" in p or "." in p:
            break

        count, adj, color = p.split()[-3:]
        bags.append((int(count), adj + " " + color))

    return bag, bags


def count_bags(bags_map):
    count = 0
    queue = [(1, "shiny gold")]

    while queue:
        qty, bag = queue.pop(0)

        for q, n in bags_map[bag]:
            queue.append((qty * q, n))
            count += qty * q

    return count


test_inpt = read_input(7, file_template="{:02}_test_2_input", line_parser=parser)
test_inpt = {k: v for k, v in test_inpt}

assert count_bags(test_inpt) == 126

inpt = read_input(7, line_parser=parser)
inpt = {k: v for k, v in inpt}

assert count_bags(inpt) == 12414
