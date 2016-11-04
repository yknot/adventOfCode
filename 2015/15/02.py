import numpy as np

data = [o.strip().split() for o in open('input').readlines()]

ingredients = {}
for line in data:
    name = line[0].strip(':')
    properties = {line[1]:int(line[2].strip(',')),
                  line[3]:int(line[4].strip(',')),
                  line[5]:int(line[6].strip(',')),
                  line[7]:int(line[8].strip(',')),
                  line[9]:int(line[10].strip(','))}


    ingredients[name] = properties


# http://mathoverflow.net/questions/9477/uniquely-generate-all-permutations-of-three-digits-that-sum-to-a-particular-value/

def multichoose(n,k):
    if k < 0 or n < 0: return "Error"
    if not k: return [[0]*n]
    if not n: return []
    if n == 1: return [[k]]
    return [[0]+val for val in multichoose(n-1,k)] + \
        [[val[0]+1]+val[1:] for val in multichoose(n,k-1)]

def calc(ingredients, amt):
    assert len(ingredients) == len(amt)
    keys = [k for k in ingredients.values()[0].keys() if k != 'calories']
    totals = [0]*len(keys)
    
    for i in range(len(amt)):
        val = ingredients[ingredients.keys()[i]]
        for j in range(len(keys)):
            totals[j] += val[keys[j]]*amt[i]

    for t in totals:
        if t < 0:
            return 0
    return np.prod(totals)

total = 100
best = 0
totalCal = 500
for amt in multichoose(len(ingredients), total):
    if np.dot([i['calories'] for i in ingredients.values()], amt) != 500:
        continue
    current = calc(ingredients, amt)
    if current > best:
        best = current


print best
