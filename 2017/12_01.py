def parse_input(data):
    node_dict = {}
    for d in data:
        node, after = d.split(' <-> ')
        node = int(node)
        node_dict[node] = [int(a) for a in after.split(', ')]

    return node_dict


def parse_list(nodes_raw):
    """take list of nodes and file all connected to 0"""
    nodes = parse_input(nodes_raw)

    connected = set([0])
    queue = [0]
    while len(queue):
        n = queue.pop(0)
        edges = nodes[n]

        for e in edges:
            if e not in connected:
                queue.append(e)
                connected.add(e)

    return len(connected)


# test
assert parse_list(open('testinput').read().splitlines()) == 6

# real input
print(parse_list(open('input').read().splitlines()))
