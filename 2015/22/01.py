import numpy as np
import copy

# debug prints
debug = False

# spell options
# mana, damage, turns, heals, armor, mana_increase
spells = np.array([
    [53, 4, 1, 0, 0, 0],  # magic missle
    [73, 2, 1, 2, 0, 0],  # drain
    [113, 0, 6, 0, 7, 0],  # shield
    [173, 3, 6, 0, 0, 0],  # poison
    [229, 0, 5, 0, 0, 101]  # recharge
])

min_usage = np.inf
for trial in range(10000000):
    # starting values
    mana = 500
    hp = 50
    armor = 0
    boss_hp = 51
    boss_damage = 9

    win = True
    cost = 0
    current_moves = []
    while True:
        # check if enough mana
        if np.all(mana < spells[:, 0]):
            if debug:
                print("not enough mana")
            win = False
            break

        # pick a move
        index = np.random.choice(spells.shape[0])
        move = copy.deepcopy(spells[index])
        # spend mana one time cost
        mana -= move[0]

        if debug:
            print("move:", end="\n\t")
            print(move)

        current_moves.append(move)
        new_moves = []
        if debug:
            print("running moves:")
        for c in current_moves:
            if debug:
                print('', end='\t')
                print(c)
            # add to total cost
            cost += c[0]
            # do damage to boss
            boss_hp -= c[1]
            # heal
            hp += c[3]
            # armor
            armor += c[4]
            # mana increase
            mana += c[5]

            # decrement turns
            c[2] -= 1
            if c[2] > 0:
                new_moves.append(c)

        # change over moves
        current_moves = new_moves

        if boss_hp <= 0:
            if debug:
                print("we win!")
            if cost < min_usage:
                print("new min")
                print(cost)
                min_usage = cost
            break

        # boss does damage
        if armor > 0:
            attack = np.max([boss_damage - armor, 1])
            hp -= attack
            armor -= boss_damage
            if armor < 0:
                armor = 0

        else:
            hp -= boss_damage

        if hp <= 0:
            if debug:
                print("we lose")
            win = False
            break
        if debug:
            print()

print("minimum usage:", end="\t")
print(min_usage)
