import re

lines = [l.strip() for l in open('input').readlines()]

replacements = []
for l in lines:
    if l.find('=>') != -1:
        splits = l.split('=>')
        replacements.append([splits[0].strip(), splits[1].strip()])
    elif len(l) != 0:
        text = l

outputs = set()

for r in replacements:
    starts = [m.start() for m in re.finditer(r[0], text)]
    for s in starts:
        outputs.add(text[:s] + r[1] + text[s+len(r[0]):])

print(len(outputs))
