import numpy as np
import copy


class Game(object):
    """type game"""
    def __init__(self, spells):
        self.mana = 500
        self.hp = 50
        self.armor = 0
        self.boss_hp = 51
        self.boss_damage = 9
        self.spells = spells

        self.player = True
        self.win = True
        self.cost = 0
        self.current_moves = []

    def check_mana(self):
        if np.all(self.mana < self.spells[:, 0]):
            self.win = False
            return False
        return True

    def get_index(self):
        index = np.random.choice(self.spells.shape[0])
        if self.spells[index][0] in [c[0] for c in self.current_moves if c[2] >= 1]:
            return self.get_index()
        else:
            return index

    def pick_move(self):
        index = self.get_index()
        move = copy.deepcopy(self.spells[index])
        # spend mana one time cost
        self.mana -= move[0]
        # add to total cost
        self.cost += move[0]
        # run player moves
        self.current_moves.append(move)

    def run_moves(self):
        new_moves = []

        for c in self.current_moves:
            # do damage to boss
            self.boss_hp -= c[1]
            # heal
            self.hp += c[3]
            # armor
            self.armor = max(i[4] for i in self.current_moves)
            # mana increase
            self.mana += c[5]

            # decrement turns
            c[2] -= 1
            if c[2] > 0:
                new_moves.append(c)
        # change over moves
        self.current_moves = new_moves

    def play(self):
        # hard difficulty
        self.hp -= 1
        if self.hp <= 0:
            self.win = False
            return False

        # check to  make sure there is enough mana left
        if not self.check_mana():
            return False

        # PLAYER MOVE
        self.pick_move()
        self.run_moves()

        if self.boss_hp <= 0:
            return False

        # BOSS TURN
        self.hp -= np.max([self.boss_damage - self.armor, 1])

        self.run_moves()

        if self.hp <= 0:
            self.win = False
            return False

        return True


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
for trial in range(100000):
    # starting values

    this_game = Game(copy.deepcopy(spells))
    while this_game.play():
        pass

    if this_game.win and this_game.cost < min_usage:
        print("new min")
        print(this_game.cost)
        min_usage = this_game.cost


print("minimum usage:", end="\t")
print(min_usage)
