data = [l.strip() for l in open('input').readlines()]

known = {'children': 3,
         'cats': 7,
         'samoyeds': 2,
         'pomeranians': 3,
         'akitas': 0,
         'vizslas': 0,
         'goldfish': 5,
         'trees': 3,
         'cars': 2,
         'perfumes': 1}

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


    if all(item in known.items() for item in facts.items()):
        print j
        aunts.append(facts)

    j += 1

