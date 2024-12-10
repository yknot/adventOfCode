from collections import defaultdict


example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def parse_data(data):
    orderings, updates = data.split("\n\n")
    orderings = [list(map(int, line.split("|"))) for line in orderings.split("\n")]
    ordering_dict = defaultdict(list)
    for k, v in orderings:
        ordering_dict[k].append(v)

    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]

    return ordering_dict, updates


def validate_update(ordering_dict, update):
    for i, u in enumerate(update):
        # check if properly before everything
        if i == len(update) - 1:
            continue

        for nxt in update[i + 1 :]:
            if nxt not in ordering_dict[u]:
                return False

        # check if properly after everything
        if i == 0:
            continue

        for prev in update[:i]:
            if u not in ordering_dict[prev]:
                return False

    return True


def check_updates(data):
    ordering_dict, updates = parse_data(data)

    total = 0
    for update in updates:
        if validate_update(ordering_dict, update):
            total += update[len(update) // 2]

    return total


def fix_update(ordering_dict, update):
    new_update = []
    while len(new_update) < len(update):
        for u in update:
            # if already in new update
            if u in new_update:
                continue

            # last in
            if len(new_update) == len(update) - 1:
                new_update.append(u)
                break

            # check if properly before everything
            rest = [x for x in update if x != u and x not in new_update]
            valid = True
            for nxt in rest:
                if nxt not in ordering_dict[u]:
                    valid = False
                    break
            if not valid:
                continue

            # first in
            if len(new_update) == 0:
                new_update.append(u)
                break

            # check if properly after everything
            valid = True
            for prev in new_update:
                if u not in ordering_dict[prev]:
                    valid = False
                    break

            if not valid:
                continue

            new_update.append(u)

    return new_update


def fix_updates(data):
    ordering_dict, updates = parse_data(data)

    total = 0
    for update in updates:
        if not validate_update(ordering_dict, update):
            fixed = fix_update(ordering_dict, update)
            total += fixed[len(fixed) // 2]

    return total


res = check_updates(example)
assert res == 143, res

with open("05_input") as f:
    res = check_updates(f.read())
    assert res == 4637, res


res = fix_updates(example)
assert res == 123, res

with open("05_input") as f:
    res = fix_updates(f.read())
    assert res == 6370, res
