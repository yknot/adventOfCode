import numpy as np
import pulp


weights = [int(o) for o in open('input').read().splitlines()]
weights = sorted(weights)[::-1]
group_total = sum(weights) / 4
N = len(weights)

# variables indexes
var_idx = [(i, j) for i in range(N) for j in range(4)]

# create a binary variable for which group each is in
x = pulp.LpVariable.dicts('idx', var_idx,
                          lowBound=0,
                          upBound=1,
                          cat=pulp.LpInteger)

group_model = pulp.LpProblem("min group problem", pulp.LpMinimize)

# objective
group_model += sum([x[idx] for idx in var_idx if idx[1] == 0])

# group total constraints
for i in range(4):
    group_model += sum([weights[idx[0]] * x[idx] for idx in var_idx
                        if idx[1] == i]) == group_total, "w_dot_" + str(i)

# each x y and z sum to 1
for i in range(28):
    group_model += sum([x[idx] for idx in var_idx if idx[0] == i]) == 1, \
        "One_per_group_" + str(i)

group_model.solve()

group_size = int(sum([x[idx].value() for idx in var_idx if idx[1] == 0]))


possible_groups = [tuple(c) for c in pulp.allcombinations(weights, group_size)
                   if np.sum(c) == group_total]

print(np.min([np.prod(group) for group in possible_groups]))
