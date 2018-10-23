"""advent of code 2016 day 11 part 1"""
from itertools import combinations, chain
from collections import defaultdict
from copy import deepcopy


class RTF(object):
    """class for Radioisotope Testing Facility"""

    def __init__(self):
        """set up floors object"""
        self.floors = {k: set() for k in range(1, 5)}
        self.loc = 1
        self.moves = []

    def __str__(self):
        """string representation of class"""
        res = 'Floors:\n\t'
        res += '{}\n\t{}\n\t{}\n\t{}\n'.format(self.floors[4],
                                               self.floors[3],
                                               self.floors[2],
                                               self.floors[1])
        res += 'Elevator Location:{}\n'.format(self.loc)
        return res

    def __hash__(self):
        return hash((frozenset(self.floors[1]), frozenset(self.floors[2]),
                     frozenset(self.floors[3]), frozenset(self.floors[4]),
                     self.loc))

    def add_chip(self, n, f):
        """add chip 'n' to floor 'f'"""
        self.floors[f].add(('chip', n))

    def add_generator(self, n, f):
        """add generator 'n' to floor 'f'"""
        self.floors[f].add(('generator', n))

    def done(self):
        """check if valid finishing condition"""
        # all objects on 4th floor and elevator
        if sum(len(v) for k, v in self.floors.items() if k != 4) == 0 and \
                self.loc == 4:
            return True
        return False

    def valid_config(self):
        """check to make sure we don't fail the configuration"""
        for _, v in self.floors.items():
            if not check_compatible(v):
                return False
        return True

    def get_next_locations(self):
        """calculate the next locations to look"""
        next_locations = []
        # start with above
        if self.loc < 4:
            next_locations.append(self.loc + 1)
        # check below
        found = False
        for i in range(1, self.loc):
            if self.floors[i]:
                found = True
                break
        # if we found one below and not first floor add
        if found and self.loc > 1:
            next_locations.append(self.loc - 1)
        return next_locations

    def possible_moves(self):
        """find all the possible moves"""
        # next locations can be up or down unless on edge
        next_locations = self.get_next_locations()
        # elevator can take 1 or 2 items
        elevator_contents = chain(combinations(self.floors[self.loc], 2),
                                  combinations(self.floors[self.loc], 1))
        valid_moves = []
        # flags for if we are skipping
        up_skip = down_skip = False
        # for all possible elevator combinations
        for e_c in elevator_contents:
            # for all possible floor movements
            for n_l in next_locations:
                # check floor the next floor combined with the elevator
                if check_compatible(self.floors[self.loc] - {e_c}) and \
                   check_compatible(self.floors[n_l].union(e_c)):
                    valid_moves.append((n_l, e_c))

                    # if going up if we are trying to move two up already skip
                    if n_l > self.loc and len(e_c) == 2:
                        up_skip = True
                    if n_l < self.loc and len(e_c) == 1:
                        down_skip = True
        # remove the up and down skips
        valid_moves_filtered = []
        for n_l, e_c in valid_moves:
            # if we can skip up then we will remove if only one
            if up_skip and n_l > self.loc and len(e_c) == 1:
                continue
            # if we can skip down then we will remove if two
            # if down_skip and n_l < self.loc and len(e_c) == 2:
            #     continue
            valid_moves_filtered.append((n_l, e_c))
        return valid_moves_filtered

    def move(self, n_l, e_c):
        """move the components"""
        self.moves.append((n_l, e_c))
        # remove from the current floor
        for e in e_c:
            self.floors[self.loc].remove(e)
        # change floor
        self.loc = n_l
        # add to new floor
        for e in e_c:
            self.floors[self.loc].add(e)


def check_compatible(options):
    """checks all possible permutations of a set"""
    options_mod = deepcopy(options)
    for i, j in combinations(options, 2):
        if i[1] == j[1]:
            if i[0] == 'chip':
                options_mod.remove(i)
            else:
                options_mod.remove(j)

    for i, j in combinations(options_mod, 2):
        if i[0] != j[0] and i[1] != j[1]:
            return False
    return True


hashes = []
equiv_hashes = []


def pairs_all_equal(rtf):
    """check to see if all chip and generator pairs are equiv"""
    elements = {}
    for k, v in rtf.floors.items():
        for i in v:
            if i[1] not in elements:
                elements[i[1]] = [None, None]
            if i[0] == 'chip':
                elements[i[1]][0] = k
            else:
                elements[i[1]][1] = k

    elements_dict = defaultdict(int)
    for c, g in elements.values():
        elements_dict[(c, g)] += 1

    elements_dict['elev'] = rtf.loc
    hash_val = hash(frozenset(elements_dict.items()))
    if hash_val in equiv_hashes:
        return True

    equiv_hashes.append(hash_val)
    return False


def runner(rtf):
    total_moves = 0
    uniq_moves = set()
    hashes.append(hash(rtf))
    queue = [(rtf, 1, m) for m in rtf.possible_moves()]

    while True:
        total_moves += 1
        if not queue:
            print("queue empty, failed")
            break
        r, c, m = queue.pop(0)
        rtf_tmp = deepcopy(r)

        rtf_tmp.move(m[0], m[1])

        # sanity check
        if not rtf_tmp.valid_config():
            continue

        # already exists continue
        if hash(rtf_tmp) in hashes:
            continue
        if pairs_all_equal(rtf_tmp):
            continue
        # else add to hashes
        hashes.append(hash(rtf_tmp))

        # if done
        if rtf_tmp.done():
            print("Done! with {} total moves".format(total_moves))
            return rtf_tmp, c

        if c not in uniq_moves:
            uniq_moves.add(c)
            print('Move {0}'.format(c))

        # add new moves
        for m in rtf_tmp.possible_moves():
            queue.append((rtf_tmp, c + 1, m))

    # didn't find the solution
    return None, None


floor_map = {'first': 1,
             'second': 2,
             'third': 3,
             'fourth': 4}
data = open('input_2').read().splitlines()

rtf = RTF()

# add info to rtf object
for d in data:
    cmd = d.split()
    floor = floor_map[cmd[1]]
    for i, c in enumerate(cmd):
        if c.find('microchip') != -1:
            name = cmd[i - 1].split('-')[0]
            rtf.add_chip(name, floor)
        elif c.find('generator') != -1:
            rtf.add_generator(cmd[i - 1], floor)

# make moves
res, count = runner(rtf)

if res:
    print("\n\n====FINAL====")
    print(res)
    # print(rtf)
    # for m in res.moves:
    #     rtf.move(*m)
    #     print(rtf)
    print("Moves: {}".format(count))
