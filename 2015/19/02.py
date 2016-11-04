from random import shuffle

lines = [l.strip() for l in open('input').readlines()]

replacements = []
for l in lines:
    if l.find('=>') != -1:
        splits = l.split('=>')
        replacements.append((splits[0].strip(), splits[1].strip()))
    elif len(l) != 0:
        goal = l

# simplify in the order provided
# if it doesn't work reset shuffle and try again
count = 0
target = goal
while target != 'e':
    changed = False
    for a, b in replacements:
        if b in target:
            target = target.replace(b, a, 1)
            count += 1
            changed = True

    if not changed:
        if target == 'e'*len(target):
            break
        target = goal
        count = 0
        shuffle(replacements)

print(count)

