"""

Day 7 part 1

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


def dig(bag, bags_map):
    # base case if directy are shiny gold or contain shiny gold
    if bag == "shiny gold":
        return True
    contains = bags_map[bag]
    if any([1 for c in contains if c[1] == "shiny gold"]):
        return True

    for c in contains:
        if dig(c[1], bags_map):
            return True

    return False


def find_bags(bags_map):
    count = 0

    for bag, contains in bags_map.items():
        # if left side is shiny gold
        if bag == "shiny gold":
            continue
        # if directly contain
        if any([1 for c in contains if c[1] == "shiny gold"]):
            count += 1
            continue
        for c in contains:
            if dig(c[1], bags_map):
                count += 1
                break

    return count


test_inpt = read_input(7, file_template="{:02}_test_input", line_parser=parser)
test_inpt = {k: v for k, v in test_inpt}

assert find_bags(test_inpt) == 4

inpt = read_input(7, line_parser=parser)
inpt = {k: v for k, v in inpt}

assert find_bags(inpt) == 211
