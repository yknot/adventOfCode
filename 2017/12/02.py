def parse_input(data):
    node_dict = {}
    for d in data:
        node, after = d.split(' <-> ')
        node = int(node)
        node_dict[node] = [int(a) for a in after.split(', ')]

    return node_dict


def consolidate(groups):
    """check for colliding groups"""
    new_groups = []
    for g in groups:
        found = 0
        for i, n in enumerate(new_groups):
            if n.intersection(g):
                new_groups[i] = n.union(g)
                found = 1
                break

        if not found:
            new_groups.append(g)

    return new_groups


def parse_list(nodes_raw):
    """take list of nodes and file all connected to 0"""
    nodes = parse_input(nodes_raw)

    connected_groups = [set([0])]
    # for each node
    for n, e in nodes.items():
        found = 0
        # try to find in a group
        for g in connected_groups:
            # if in a group
            if n in g or g.intersection(set(e)):
                # add all other nodes to that group
                for edge in e:
                    g.add(edge)
                g.add(n)
                found = 1
                break
        if not found:
            connected_groups.append(set([n] + e))

    # one last attempt to consolidate the connected groups
    prev = 0
    while True:
        connected_groups = consolidate(connected_groups)
        if len(connected_groups) == prev:
            break
        prev = len(connected_groups)

    return connected_groups


# test
assert len(parse_list(open('testinput').read().splitlines())) == 2

# real input
print(len(parse_list(open('input').read().splitlines())))
