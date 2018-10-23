import numpy as np
import sys


def read_in_tree(filename):
    """read in the tree into weights and branch lists"""
    weights = {}
    branches = {}
    for l in open(filename).read().split('\n'):
        l_split = l.split()
        weights[l_split[0]] = int(l_split[1].strip('()'))
        if len(l_split) == 2:
            continue
        branches[l_split[0]] = [p.strip(',') for p in l_split[3:]]

    return weights, branches


def find_root(branches):
    """find the root given the branches"""
    # for all possible roots
    for root in branches.keys():
        found = False
        # check branches
        for nodes in branches.values():
            # if found then not root
            if root in nodes:
                found = True
                break
        # found means not root
        if found:
            continue
        return root


def post_order(weights, branches, root):
    """do a post order traversal checking the weights as you go"""

    nodes = branches[root]
    n_wgts = np.zeros(len(nodes))
    b_wgts = np.zeros(len(nodes))
    for i, n in enumerate(nodes):
        # get the node weight
        n_wgts[i] = weights[n]

        # get branches weight if possible
        if n in branches:
            res, flag = post_order(weights, branches, n)
            if flag:
                return res, flag
            b_wgts[i] = res

    c_wgts = n_wgts + b_wgts
    if len(np.unique(c_wgts)) == 1:
        return np.sum(c_wgts), False
    else:
        totals, counts = np.unique(c_wgts, return_counts=True)
        actual_loc = counts.tolist().index(1)
        goal = totals[actual_loc - 1]
        node_loc = c_wgts.tolist().index(totals[actual_loc])
        return int(goal - b_wgts[node_loc]), True


w, b = read_in_tree('test_input')
r = find_root(b)
assert r == 'tknk'
assert post_order(w, b, r)[0] == 60

w, b = read_in_tree('input')
r = find_root(b)
assert r == 'aapssr'
print(post_order(w, b, r)[0])
