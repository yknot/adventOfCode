import numpy as np
import itertools


def fight(you, boss):
    """run the fight to see who wins"""
    you_attack = you['damage'] - boss['armor']
    if you_attack < 1:
        you_attack = 1
    boss_attack = boss['damage'] - you['armor']
    if boss_attack < 1:
        boss_attack = 1
    boss_turns = np.ceil(you['hit']/boss_attack)
    you_turns = np.ceil(boss['hit']/you_attack)
    return you_turns <= boss_turns

# input
you = {}
boss = {}
you['hit'] = 100
boss['hit'] = 100
boss['damage'] = 8
boss['armor'] = 2

weapons = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]
armors = [(13, 1), (31, 2), (53, 3), (75, 4), (102, 5), (0, 0)]
rings_damage = [(25, 1), (50, 2), (100, 3), (0, 0)]
rings_armor = [(20, 1), (40, 2), (80, 3), (0, 0)]

highest = 0
iterable = itertools.product(range(len(weapons)),
                             range(len(armors)),
                             range(len(rings_damage) + len(rings_armor)),
                             range(len(rings_damage) + len(rings_armor)))
for weapon_id, armor_id, r1, r2 in iterable:
    if r1 == r2:
        continue
    cost = 0
    cost += weapons[weapon_id][0]
    you['damage'] = weapons[weapon_id][1]

    cost += armors[armor_id][0]
    you['armor'] = armors[armor_id][1]

    rings_ids = [r1, r2]
    for r in rings_ids:
        if r <= 3:
            cost += rings_damage[r][0]
            you['damage'] += rings_damage[r][1]
        else:
            cost += rings_armor[r % len(rings_damage)][0]
            you['armor'] += rings_armor[r % len(rings_damage)][1]

    if not fight(you, boss) and cost > highest:
        highest = cost

print(highest)
