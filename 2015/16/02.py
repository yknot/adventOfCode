import copy

data = [l.strip() for l in open('input').readlines()]

known = {'children': 3,
#         'cats': 7,           # greater than
         'samoyeds': 2,
#         'pomeranians': 3,    # less than
         'akitas': 0,
         'vizslas': 0,
#         'goldfish': 5,       # less than
#         'trees': 3,          # greater than
         'cars': 2,
         'perfumes': 1}
gtKnown = {'cats':7,
           'trees':3}
ltKnown = {'pomeranians': 3,
           'goldfish': 5}


def checkEqual(known, facts):
    temp = copy.deepcopy(facts)
    for key in ['cats', 'trees', 'pomeranians', 'goldfish']:
        if key in temp:
            temp.pop(key)
    return all(item in known.items() for item in temp.items())

def checkLess(known, facts):
    for key, value in known.items():
        if key in facts.keys():
            if value <= facts[key]:
                return False

    return True


def checkGreater(known, facts):
    for key, value in known.items():
        if key in facts.keys():
            if value >= facts[key]:
                return False

    return True



aunts = []
j = 1
for d in data:
    facts = {}
    d = d.split()[2:]
    flag = False
    name = ''
    value = 0
    for i in d:
        if flag:
            value = int(i.strip(','))
            facts[name] = value
            flag = False
        else:
            name = i.strip(':')
            flag = True

            
    if checkEqual(known, facts):
        print 'almost ' + str(j)
        if checkLess(ltKnown, facts):
            print 'almost again ' + str(j)
            if checkGreater(gtKnown, facts):
                print 'almost again again' + str(j)
                aunts.append(facts)

    j += 1

